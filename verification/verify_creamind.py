
from playwright.sync_api import sync_playwright

def verify_creamind():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Files to verify
        files = ['index.html', 'blog.html', 'contact.html', 'cv.html', 'portfolio.html', 'podcast.html', 'components.html', 'typography.html', 'navigation.html']

        for file in files:
            print(f'Verifying {file}...')
            page.goto(f'file:///app/public/{file}')

            # Take screenshot
            page.screenshot(path=f'verification/verified_{file}.png', full_page=True)
            print(f'Screenshot saved to verification/verified_{file}.png')

        browser.close()

if __name__ == '__main__':
    verify_creamind()
