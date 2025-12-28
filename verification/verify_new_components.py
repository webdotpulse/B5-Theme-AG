from playwright.sync_api import sync_playwright, expect
import os

def test_new_components():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to example page
        base_dir = os.path.abspath('public')
        url = f'file://{base_dir}/example-page.html'
        print(f"Navigating to {url}")
        page.goto(url)

        # Verify page title
        expect(page).to_have_title("Example Page | Arsela Gjonaj")

        # Verify specific components are present
        expect(page.locator('.flip-card').first).to_be_visible()
        expect(page.locator('.process-steps')).to_be_visible()
        expect(page.locator('.skill-bar-wrapper').first).to_be_visible()
        expect(page.locator('.avatar-group')).to_be_visible()
        expect(page.locator('.chat-widget')).to_be_visible()

        # Take screenshot
        output_path = 'verification/verified_example_page.png'
        page.screenshot(path=output_path, full_page=True)
        print(f"Screenshot saved to {output_path}")

        browser.close()

if __name__ == '__main__':
    test_new_components()
