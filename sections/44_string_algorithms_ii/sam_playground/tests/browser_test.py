"""Exercise the standalone page in Chromium, including file:// and mobile layout.

Requires Chromium and the Python websocket-client package. No HTTP server or
third-party browser driver is needed. Screenshots are written to /tmp.
"""
from pathlib import Path
import json
import shutil
import subprocess
import tempfile
import time
import urllib.request

import websocket

PAGE = Path(__file__).resolve().parents[1] / 'index.html'


class Browser:
    def __init__(self, executable, directory):
        self.process = subprocess.Popen([
            executable, '--headless=new', '--no-sandbox', '--disable-gpu',
            '--disable-dev-shm-usage', '--no-first-run',
            '--no-default-browser-check', '--disable-background-networking',
            '--disable-component-update', '--disable-sync', '--disable-extensions',
            '--remote-debugging-port=0', '--remote-allow-origins=*',
            f'--user-data-dir={directory}', 'about:blank',
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.socket = None
        self.serial = 0
        self.errors = []
        port_file = Path(directory) / 'DevToolsActivePort'
        deadline = time.monotonic() + 15
        while not port_file.exists():
            if self.process.poll() is not None:
                raise RuntimeError('Chromium exited before opening its debugging port')
            if time.monotonic() > deadline:
                raise TimeoutError('Chromium did not open its debugging port')
            time.sleep(.05)
        port = port_file.read_text().splitlines()[0]
        with urllib.request.urlopen(f'http://127.0.0.1:{port}/json/list') as response:
            tabs = json.load(response)
        tab = next(tab for tab in tabs if tab['type'] == 'page')
        self.socket = websocket.create_connection(tab['webSocketDebuggerUrl'], timeout=10)
        self.call('Runtime.enable')
        self.call('Page.enable')
        self.call('Emulation.setDeviceMetricsOverride', {
            'width': 1440, 'height': 1100, 'deviceScaleFactor': 1, 'mobile': False,
        })
        self.call('Page.navigate', {'url': PAGE.as_uri()})
        deadline = time.monotonic() + 10
        while not self.evaluate('Boolean(globalThis.samPlayground)'):
            if time.monotonic() > deadline:
                raise TimeoutError('Page did not initialize')
            time.sleep(.05)

    def call(self, method, params=None):
        self.serial += 1
        current = self.serial
        self.socket.send(json.dumps({'id': current, 'method': method, 'params': params or {}}))
        while True:
            message = json.loads(self.socket.recv())
            if message.get('method') == 'Runtime.exceptionThrown':
                self.errors.append(message['params']['exceptionDetails'])
            if message.get('id') == current:
                if 'error' in message:
                    raise RuntimeError(message['error'])
                return message.get('result', {})

    def evaluate(self, expression):
        result = self.call('Runtime.evaluate', {
            'expression': expression, 'returnByValue': True, 'awaitPromise': True,
        })
        if 'exceptionDetails' in result:
            raise RuntimeError(result['exceptionDetails'])
        return result.get('result', {}).get('value')

    def fill(self, identifier, value):
        self.evaluate(f'document.getElementById({json.dumps(identifier)}).value = {json.dumps(value)}')

    def click(self, identifier):
        point = self.evaluate(f'''(() => {{
            const node = document.getElementById({json.dumps(identifier)});
            node.scrollIntoView({{block: "center"}});
            const r = node.getBoundingClientRect();
            return {{x: r.x + r.width / 2, y: r.y + r.height / 2}};
        }})()''')
        self.call('Input.dispatchMouseEvent', {'type': 'mousePressed', 'button': 'left', 'clickCount': 1, **point})
        self.call('Input.dispatchMouseEvent', {'type': 'mouseReleased', 'button': 'left', 'clickCount': 1, **point})

    def frame(self):
        return self.evaluate('samPlayground.getFrame()')

    def load(self, text):
        self.fill('source-input', text)
        self.click('load-button')

    def finish(self, letters):
        for _ in range(letters):
            self.click('letter-button')

    def screenshot(self, path):
        import base64
        self.evaluate('window.scrollTo(0, 0)')
        metrics = self.call('Page.getLayoutMetrics')['cssContentSize']
        result = self.call('Page.captureScreenshot', {
            'format': 'png', 'captureBeyondViewport': True,
            'clip': {'x': 0, 'y': 0, 'width': metrics['width'], 'height': metrics['height'], 'scale': 1},
        })
        Path(path).write_bytes(base64.b64decode(result['data']))

    def close(self):
        if self.socket:
            self.socket.close()
        self.process.terminate()
        try:
            self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait()


def main():
    executable = shutil.which('chromium') or shutil.which('google-chrome')
    if not executable:
        raise RuntimeError('Chromium is required for these checks')
    with tempfile.TemporaryDirectory(prefix='sam-chromium-') as directory:
        browser = Browser(executable, directory)
        try:
            assert browser.frame()['text'] == []
            assert browser.evaluate('document.querySelectorAll(".code-line.active").length') == 0
            browser.click('next-button')
            assert browser.frame()['line'] == 1
            assert browser.evaluate('document.querySelector(".code-line.active").dataset.line') == '1'
            browser.click('prev-button')
            assert browser.evaluate('samPlayground.getCursor()') == 0
            browser.finish(5)
            frame = browser.frame()
            assert ''.join(frame['text']) == 'abcbc'
            assert len(frame['states']) == 8 and frame['last'] == 6 and frame['distinct'] == 12
            assert browser.evaluate('document.getElementById("next-button").disabled')
            final = browser.evaluate('JSON.stringify(samPlayground.getFrame())')
            for _ in range(3): browser.click('prev-button')
            for _ in range(3): browser.click('next-button')
            assert browser.evaluate('JSON.stringify(samPlayground.getFrame())') == final
            browser.evaluate('document.querySelector("#state-table [data-state=\\"7\\"]").click()')
            assert '{3, 5}' in browser.evaluate('document.getElementById("inspector").textContent')
            assert '= 2 sous-chaine' in browser.evaluate('document.getElementById("inspector").textContent')
            assert browser.evaluate('document.querySelectorAll("#graph path[stroke=\\"#456cbe\\"]").length') == 7
            browser.click('show-links')
            assert browser.evaluate('document.querySelectorAll("#graph path[stroke=\\"#456cbe\\"]").length') == 0
            browser.click('show-links')
            browser.click('zoom-fit')
            browser.screenshot('/tmp/sam-playground-desktop.png')
            browser.fill('append-input', 'd')
            browser.click('append-button')
            assert browser.evaluate('samPlayground.getTarget()') == 'abcbcd'
            browser.finish(1)
            assert browser.frame()['distinct'] == 18
            assert browser.frame()['states'][7]['next']['d'] == 8
            browser.load('abcbc')
            browser.click('next-button')
            browser.click('next-button')
            old_cursor = browser.evaluate('samPlayground.getCursor()')
            browser.fill('append-input', 'd')
            browser.click('append-button')
            assert browser.evaluate('samPlayground.getCursor()') == old_cursor
            browser.finish(6)
            assert ''.join(browser.frame()['text']) == 'abcbcd'
            assert browser.frame()['distinct'] == 18
            browser.load('')
            assert browser.evaluate('document.getElementById("next-button").disabled')
            assert browser.frame()['distinct'] == 0
            browser.load('\U0001f600a\U0001f600')
            browser.finish(3)
            assert browser.frame()['distinct'] == 5
            assert len(browser.frame()['text']) == 3
            browser.load('<>&"')
            browser.finish(4)
            assert ''.join(browser.frame()['text']) == '<>&"'
            assert browser.evaluate('document.querySelectorAll("script").length') == 2
            browser.load('abb')
            browser.fill('speed', '100')
            browser.evaluate('document.getElementById("speed").dispatchEvent(new Event("input"))')
            browser.click('play-button')
            deadline = time.monotonic() + 3
            while browser.evaluate('samPlayground.getCursor()') < 2:
                assert time.monotonic() < deadline
                time.sleep(.05)
            browser.click('play-button')
            stopped = browser.evaluate('samPlayground.getCursor()')
            time.sleep(.2)
            assert browser.evaluate('samPlayground.getCursor()') == stopped
            browser.finish(3)
            assert browser.frame()['distinct'] == 5
            assert browser.frame()['states'][4]['cloneOf'] == 2
            browser.evaluate('document.getElementById("timeline").value=0; document.getElementById("timeline").dispatchEvent(new Event("input"))')
            assert browser.evaluate('samPlayground.getCursor()') == 0
            browser.evaluate('document.getElementById("timeline").value=document.getElementById("timeline").max; document.getElementById("timeline").dispatchEvent(new Event("input"))')
            assert browser.frame()['distinct'] == 5
            browser.call('Emulation.setDeviceMetricsOverride', {
                'width': 390, 'height': 844, 'deviceScaleFactor': 1, 'mobile': False,
            })
            assert browser.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 1'), browser.evaluate('({width:innerWidth,scroll:document.documentElement.scrollWidth,wide:[...document.querySelectorAll("body *")].filter(n=>n.getBoundingClientRect().right>innerWidth+1).slice(0,15).map(n=>({tag:n.tagName,id:n.id,class:n.className,right:n.getBoundingClientRect().right}))})')
            browser.evaluate('new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))')
            browser.screenshot('/tmp/sam-playground-mobile.png')
            assert not browser.errors, browser.errors
            print('Browser: navigation, active lines, variables, rewind, clones, append mid-step, playback, Unicode, safe text and mobile layout pass offline.')
        finally:
            browser.close()


if __name__ == '__main__':
    main()
