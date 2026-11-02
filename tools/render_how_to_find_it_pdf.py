"""Render the HTML/SVG discovery manual to PDF without dropping its figures.

Requires Quarto, Chromium, and the Python websocket-client package.
Use --skip-html to print an already up-to-date HOW_TO_FIND_IT.html.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
import urllib.request

import websocket


ROOT = Path(__file__).resolve().parents[1]
PRINT_CSS = r"""
@page { size: A4; margin: 17mm 14mm; }
@media print {
  html { font-size: 14px !important; }
  html, body { background: white !important; color: #111 !important; }
  body { font-size: 10.5pt !important; line-height: 1.42 !important; }
  #quarto-content, .page-columns, .page-rows-contents {
    display: block !important; max-width: none !important;
    width: auto !important; padding: 0 !important; margin: 0 !important;
  }
  main.content {
    display: block !important; max-width: none !important;
    width: 100% !important; margin: 0 !important; padding: 0 !important;
  }
  #quarto-margin-sidebar, #quarto-sidebar, #quarto-header,
  .quarto-navigation-tool, .code-copy-button, .anchorjs-link,
  .quarto-title-meta, .toc-actions, .quarto-alternate-formats {
    display: none !important;
  }
  #title-block-header { margin: 0 0 16mm !important; }
  #title-block-header .title { font-size: 27pt !important; }
  #title-block-header .subtitle { font-size: 14pt !important; }
  h1 {
    break-before: page; break-after: avoid;
    font-size: 19pt !important; margin: 0 0 7mm !important;
    border-bottom: 1px solid #ccc; padding-bottom: 3mm;
  }
  h2, h3, h4, h5 { break-after: avoid; }
  h2 { font-size: 14pt !important; margin-top: 8mm !important; }
  h3 { font-size: 11.5pt !important; margin-top: 6mm !important; }
  p, li { orphans: 3; widows: 3; }
  p { margin-bottom: 3mm; }
  a { color: inherit !important; text-decoration: none !important; }
  .diagram-box {
    break-inside: avoid; padding: 3mm 2mm !important;
    margin: 5mm 0 !important; border-width: 1px !important;
    box-shadow: none !important; overflow: visible !important;
  }
  .diagram-title { font-size: 10pt !important; margin-bottom: 3mm; }
  .diagram-caption { font-size: 8.5pt !important; line-height: 1.3; }
  svg { max-width: 100% !important; height: auto; max-height: 190mm; }
  .pause-box, .formula-card { break-inside: avoid; }
  .pause-box, .formula-card { padding: 3mm !important; margin: 4mm 0; }
  .formula-card { font-size: 10pt !important; overflow: visible; }
  .discovery-loop { gap: 1mm; margin: 3mm 0; }
  .loop-step { padding: 1mm 2mm; font-size: 8pt; }
  table { width: 100% !important; font-size: 9pt; break-inside: auto; }
  thead { display: table-header-group; }
  tr { break-inside: avoid; }
  th, td { padding: 1.5mm 2mm !important; overflow-wrap: anywhere; }
  pre, pre code, .sourceCode {
    white-space: pre-wrap !important; overflow-wrap: anywhere !important;
    word-break: normal !important; overflow: visible !important;
  }
  pre, code { font-size: 8.5pt !important; }
  pre code { background: transparent !important; }
  .sourceCode { break-inside: auto; }
  math { font-size: 1em; }
  .pdf-contents ol { padding-left: 5mm; }
  .pdf-contents li { break-inside: avoid; margin-bottom: 2mm; }
  .pdf-contents a { font-size: 9.5pt; }
  * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
}
"""


class Browser:
    def __init__(self, executable: str, profile: Path):
        self.process = subprocess.Popen([
            executable, '--headless=new', '--no-sandbox', '--disable-gpu',
            '--disable-dev-shm-usage', '--no-first-run',
            '--no-default-browser-check', '--disable-background-networking',
            '--disable-component-update', '--disable-sync', '--disable-extensions',
            '--remote-debugging-port=0', '--remote-allow-origins=*',
            f'--user-data-dir={profile}', 'about:blank',
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.socket = None
        self.serial = 0
        port_file = profile / 'DevToolsActivePort'
        deadline = time.monotonic() + 20
        while not port_file.exists():
            if self.process.poll() is not None:
                raise RuntimeError('Chromium exited before starting its debugger')
            if time.monotonic() > deadline:
                raise TimeoutError('Chromium debugger did not start')
            time.sleep(.05)
        port = port_file.read_text().splitlines()[0]
        with urllib.request.urlopen(f'http://127.0.0.1:{port}/json/list') as response:
            tabs = json.load(response)
        tab = next(tab for tab in tabs if tab['type'] == 'page')
        self.socket = websocket.create_connection(
            tab['webSocketDebuggerUrl'], timeout=180)
        self.call('Page.enable')
        self.call('Runtime.enable')
        # The rendered document embeds its resources; printing stays offline.
        self.call('Network.enable')
        self.call('Network.setBlockedURLs', {'urls': ['http://*', 'https://*']})

    def call(self, method: str, params=None):
        self.serial += 1
        request_id = self.serial
        self.socket.send(json.dumps({
            'id': request_id, 'method': method, 'params': params or {}}))
        while True:
            response = json.loads(self.socket.recv())
            if response.get('id') == request_id:
                if 'error' in response:
                    raise RuntimeError(response['error'])
                return response.get('result', {})

    def evaluate(self, expression: str):
        result = self.call('Runtime.evaluate', {
            'expression': expression, 'returnByValue': True, 'awaitPromise': True})
        if 'exceptionDetails' in result:
            raise RuntimeError(result['exceptionDetails'])
        return result.get('result', {}).get('value')

    def close(self):
        if self.socket is not None:
            self.socket.close()
        self.process.terminate()
        try:
            self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait()


def render_pdf(html: Path, output: Path):
    chromium = shutil.which('chromium') or shutil.which('google-chrome')
    if chromium is None:
        raise RuntimeError('Chromium is required to preserve the HTML diagrams')
    with tempfile.TemporaryDirectory(prefix='discovery-print-') as directory:
        browser = Browser(chromium, Path(directory))
        try:
            browser.call('Emulation.setDeviceMetricsOverride', {
                'width': 688, 'height': 995, 'deviceScaleFactor': 1,
                'mobile': False})
            browser.call('Emulation.setEmulatedMedia', {'media': 'print'})
            browser.call('Page.navigate', {'url': html.resolve().as_uri()})
            deadline = time.monotonic() + 45
            while not browser.evaluate(
                    "document.readyState === 'complete' && Boolean(document.querySelector('main svg'))"):
                if time.monotonic() > deadline:
                    raise TimeoutError('The rendered manual did not finish loading')
                time.sleep(.1)
            browser.evaluate('document.fonts.ready.then(() => true)')
            browser.evaluate('''(() => {
                const main = document.querySelector('main');
                const contents = document.createElement('section');
                contents.className = 'pdf-contents';
                const title = document.createElement('h1');
                title.textContent = 'Contents';
                contents.append(title);
                const list = document.createElement('ol');
                main.querySelectorAll('section.level1 > h1').forEach(heading => {
                    const item = document.createElement('li');
                    const link = document.createElement('a');
                    link.href = '#' + (heading.id || heading.parentElement.id);
                    link.textContent = heading.textContent;
                    item.append(link);
                    list.append(item);
                });
                contents.append(list);
                const titleBlock = main.querySelector('#title-block-header');
                if (titleBlock) titleBlock.after(contents);
                else main.prepend(contents);
                return true;
            })()''')
            browser.evaluate('''(() => {
                const style = document.createElement('style');
                style.textContent = ''' + json.dumps(PRINT_CSS) + ''';
                document.head.append(style);
                return true;
            })()''')
            counts = browser.evaluate('''(() => {
                const main = document.querySelector('main');
                return {
                    diagrams: main.querySelectorAll('.diagram-box').length,
                    svg: main.querySelectorAll('svg').length,
                    formulas: main.querySelectorAll('math').length,
                    chapters: main.querySelectorAll('section.level1 > h1').length,
                    contentsEntries: main.querySelectorAll('.pdf-contents a').length
                };
            })()''')
            assert counts['diagrams'] == counts['svg'] > 0, counts
            assert counts['chapters'] == counts['contentsEntries'] > 0, counts
            print('Printing complete manual:', counts, flush=True)
            result = browser.call('Page.printToPDF', {
                'printBackground': True, 'preferCSSPageSize': True,
                'paperWidth': 210 / 25.4, 'paperHeight': 297 / 25.4,
                'marginTop': 17 / 25.4, 'marginBottom': 17 / 25.4,
                'marginLeft': 14 / 25.4, 'marginRight': 14 / 25.4,
                'displayHeaderFooter': True,
                'headerTemplate': '<span></span>',
                'footerTemplate': '<div style="font-size:8px;width:100%;text-align:center;color:#555"><span class="pageNumber"></span></div>',
                'generateDocumentOutline': True,
                'transferMode': 'ReturnAsStream',
            })
            handle = result['stream']
            output.parent.mkdir(parents=True, exist_ok=True)
            # Replace the previous PDF only after a complete print succeeds.
            pending = output.with_suffix('.pdf.tmp')
            try:
                with pending.open('wb') as file:
                    while True:
                        chunk = browser.call('IO.read', {'handle': handle})
                        data = chunk.get('data', '')
                        file.write(base64.b64decode(data) if chunk.get('base64Encoded')
                                   else data.encode())
                        if chunk.get('eof'):
                            break
                browser.call('IO.close', {'handle': handle})
                assert pending.stat().st_size > 1000
                pending.replace(output)
            finally:
                pending.unlink(missing_ok=True)
            print(f'Created {output} ({output.stat().st_size:,} bytes)', flush=True)
        finally:
            browser.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skip-html', action='store_true')
    args = parser.parse_args()
    html = ROOT / 'HOW_TO_FIND_IT.html'
    if not args.skip_html:
        environment = os.environ.copy()
        environment.setdefault('XDG_CACHE_HOME', str(Path(tempfile.gettempdir()) / 'quarto-discovery-cache'))
        subprocess.run(['quarto', 'render', 'HOW_TO_FIND_IT.qmd', '--to', 'html'],
                       cwd=ROOT, env=environment, check=True)
        # Quarto emits a few insignificant trailing spaces in its scripts.
        html.write_text('\n'.join(line.rstrip(' \t')
                                  for line in html.read_text().splitlines()) + '\n')
    if not html.exists():
        raise FileNotFoundError(html)
    render_pdf(html, ROOT / 'HOW_TO_FIND_IT.pdf')


if __name__ == '__main__':
    main()
