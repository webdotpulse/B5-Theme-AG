
from playwright.sync_api import sync_playwright, expect
import os

def test_creamind_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the file
        file_path = f"file://{os.getcwd()}/public/index.html"
        print(f"Navigating to {file_path}")
        page.goto(file_path)

        # Verify Title
        expect(page).to_have_title("Creamind | Turn Admiration Into Interaction")

        # Verify Header Text
        expect(page.get_by_text("Turn Admiration Into")).to_be_visible()
        expect(page.get_by_role("heading", name="Turn Admiration Into Interaction")).to_be_visible()

        # Verify Navbar
        expect(page.get_by_role("link", name="CREAMIND")).to_be_visible()
        # It's an anchor tag styled as a button
        expect(page.get_by_text("Login / Register")).to_be_visible()

        # Verify Popular Users
        expect(page.get_by_role("heading", name="Popular Users")).to_be_visible()
        expect(page.get_by_text("Melissa Harper")).to_be_visible()

        # Verify Special Features
        expect(page.get_by_role("heading", name="What Makes Creamind Special!")).to_be_visible()
        expect(page.get_by_text("Single Reply")).to_be_visible()

        # Take Screenshot
        screenshot_path = "verification/verification_creamind.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_creamind_homepage()
