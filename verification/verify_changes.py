
from playwright.sync_api import sync_playwright
import os

def run():
    # Get the absolute path to index.html
    cwd = os.getcwd()
    file_url = f"file://{cwd}/public/index.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 800})

        print(f"Navigating to {file_url}")
        page.goto(file_url)

        # Wait for animation to start (it uses requestAnimationFrame, so a small delay is good)
        page.wait_for_timeout(2000)

        # Take screenshot
        screenshot_path = "verification/index_screenshot.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()
