from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # Assume absolute path
        path = os.path.abspath("public/navigation.html")
        print(f"Navigating to file://{path}")
        page.goto(f"file://{path}")
        page.screenshot(path="screenshots/navigation.png", full_page=True)
        print("Screenshot saved to screenshots/navigation.png")
        browser.close()

if __name__ == "__main__":
    run()
