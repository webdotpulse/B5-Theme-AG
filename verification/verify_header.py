
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Since we are using static files, we can use file:// protocol.
        # We need absolute path.
        cwd = os.getcwd()
        page.goto(f'file://{cwd}/public/index.html')

        # Take screenshot of the whole page
        page.screenshot(path='verification/frontend_verify.png', full_page=True)
        print('Screenshot saved to verification/frontend_verify.png')
        browser.close()

if __name__ == '__main__':
    run()
