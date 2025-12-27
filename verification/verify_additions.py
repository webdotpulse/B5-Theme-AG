from playwright.sync_api import sync_playwright
import os

def verify_additions():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Verify Icons Page
        icons_path = os.path.abspath("public/icons.html")
        page.goto(f"file://{icons_path}")
        page.screenshot(path="verification/verified_icons.png", full_page=True)
        print("Verified icons.html")

        # Verify Code Examples Page
        code_path = os.path.abspath("public/code-examples.html")
        page.goto(f"file://{code_path}")
        page.screenshot(path="verification/verified_code_examples.png", full_page=True)
        print("Verified code-examples.html")

        browser.close()

if __name__ == "__main__":
    verify_additions()
