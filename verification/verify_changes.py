from playwright.sync_api import sync_playwright, expect
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine the absolute path to public/index.html
        cwd = os.getcwd()
        index_path = f"file://{cwd}/public/index.html"

        print(f"Navigating to: {index_path}")
        page.goto(index_path)

        # Verify the title
        expect(page).to_have_title("About Me | Arsela Gjonaj")

        # Verify the navbar link to Components exists
        components_link = page.get_by_role("link", name="Components")
        expect(components_link).to_be_visible()

        # Verify the logo text is correct
        logo = page.get_by_role("link", name="Arsela Gjonaj")
        expect(logo).to_be_visible()
        expect(logo).to_have_class("navbar-brand fw-bold text-primary")

        # Take a screenshot of the index page to verify header removal and navbar
        page.screenshot(path="verification/index_screenshot.png")
        print("Screenshot saved to verification/index_screenshot.png")

        # Navigate to Components page
        components_path = f"file://{cwd}/public/components.html"
        page.goto(components_path)

        # Verify title
        expect(page).to_have_title("Components | Arsela Gjonaj")

        # Take a screenshot of components page
        page.screenshot(path="verification/components_screenshot.png")
        print("Screenshot saved to verification/components_screenshot.png")

        browser.close()

if __name__ == "__main__":
    run()
