from playwright.sync_api import sync_playwright
import os

def take_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to the public directory
        cwd = os.getcwd()
        base_url = f"file://{cwd}/public/"

        pages = [
            "index.html",
            "cv.html",
            "portfolio.html",
            "podcast.html",
            "blog.html",
            "contact.html",
            "typography.html"
        ]

        # Ensure directory exists
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        for page_name in pages:
            url = base_url + page_name
            print(f"Navigating to {url}")
            page.goto(url)

            # Wait for any potential animations or fonts to load
            page.wait_for_timeout(1000)

            screenshot_path = f"screenshots/{page_name.replace('.html', '.png')}"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    take_screenshots()
