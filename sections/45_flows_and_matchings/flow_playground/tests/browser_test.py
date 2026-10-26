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
        while not self.evaluate('Boolean(globalThis.flowPlayground)'):
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
        return self.evaluate('flowPlayground.getFrame()')

    def load(self, text):
        self.fill('graph-input', text)
        self.click('load-button')

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
        raise RuntimeError('Chromium is required')
    with tempfile.TemporaryDirectory(prefix='flow45-browser-') as directory:
        browser = Browser(executable, directory)
        try:
            assert browser.frame()['total'] == 0
            browser.click('next-button')
            assert browser.evaluate('document.querySelectorAll(".code-line.active").length') == 1
            browser.click('previous-button')
            assert browser.frame()['phase'] == 0
            for total in (2, 4, 5):
                browser.click('augment-button')
                assert browser.frame()['total'] == total
            browser.click('finish-button')
            assert browser.frame()['done'] and browser.frame()['total'] == 5
            assert 'capacity = 5' in browser.evaluate('document.getElementById("cut-summary").textContent')
            last = browser.evaluate('JSON.stringify(flowPlayground.getFrame())')
            browser.click('previous-button')
            browser.click('next-button')
            assert browser.evaluate('JSON.stringify(flowPlayground.getFrame())') == last
            browser.fill('preset', '1')
            browser.evaluate('document.getElementById("preset").dispatchEvent(new Event("change"))')
            browser.click('augment-button')
            assert browser.frame()['total'] == 1
            for _ in range(300):
                browser.click('next-button')
                f = browser.frame()
                if f['message'].startswith('Follow') and any(e % 2 for e in f['path']):
                    break
            else:
                raise AssertionError('No reverse-edge path was displayed')
            browser.screenshot('/tmp/flow45-cancellation-desktop.png')
            browser.click('finish-button')
            assert browser.frame()['total'] == 2 and browser.frame()['done']
            browser.click('residual-toggle')
            assert '1/1' in browser.evaluate('document.getElementById("graph").textContent')
            browser.click('matching-tab')
            browser.click('augment-button')
            assert browser.frame()['total'] == 1
            for _ in range(100):
                browser.click('next-button')
                if browser.frame()['provisional']:
                    break
            assert not browser.evaluate('document.getElementById("notice").hidden')
            browser.click('finish-button')
            assert browser.frame()['left'] == [1, 0]
            assert browser.frame()['right'] == [1, 0]
            browser.screenshot('/tmp/flow45-matching-desktop.png')
            browser.load('3 2 0')
            browser.click('finish-button')
            assert browser.frame()['total'] == 0 and browser.frame()['done']
            browser.load('2 2 1\n0 9')
            assert browser.evaluate('document.getElementById("input-error").textContent')
            browser.click('flow-tab')
            browser.fill('speed', '10')
            browser.click('play-button')
            assert browser.evaluate('document.getElementById("play-button").textContent') == 'Pause'
            browser.evaluate('new Promise(resolve => setTimeout(resolve, 450))')
            browser.click('play-button')
            assert browser.frame()['phase'] >= 1
            browser.call('Emulation.setDeviceMetricsOverride', {
                'width': 390, 'height': 844, 'deviceScaleFactor': 1, 'mobile': True,
            })
            browser.screenshot('/tmp/flow45-mobile.png')
            assert browser.evaluate('document.documentElement.scrollWidth <= innerWidth + 1')
            browser.click('finish-button')
            assert browser.frame()['total'] == 5
            browser.evaluate('document.getElementById("code").scrollIntoView({block:"center"})')
            assert browser.evaluate('Boolean(document.querySelector(".code-line.active"))')
            assert not browser.errors, browser.errors
            print('Accepted: offline browser controls, cancellation, matching flips, errors, playback and mobile layout.')
        finally:
            browser.close()


if __name__ == '__main__':
    main()
