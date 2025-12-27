
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify Maintenance Page
        print("Verifying Maintenance Page...")
        page.goto(f"file://{os.path.abspath('public/maintenance.html')}")
        assert "Under Maintenance" in page.content()
        page.screenshot(path="verification/verified_maintenance.png")
        print("Maintenance page verified and screenshot taken.")

        # Verify Doodles Page
        print("Verifying Doodles Page...")
        page.goto(f"file://{os.path.abspath('public/doodles.html')}")

        # Scroll to the new section
        element = page.locator("text=File-based Doodles")
        if element.is_visible():
            element.scroll_into_view_if_needed()
        else:
            print("Warning: 'File-based Doodles' text not found immediately.")

        # Take a full page screenshot or just the bottom part where new doodles are
        page.screenshot(path="verification/verified_doodles_full.png", full_page=True)
        print("Doodles page verified and screenshot taken.")

        browser.close()

if __name__ == "__main__":
    if not os.path.exists("verification"):
        os.makedirs("verification")
    run()
