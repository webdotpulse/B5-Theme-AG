from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify Login Page
        print("Verifying Login Page...")
        page.goto(f"file://{os.getcwd()}/public/login.html")
        page.screenshot(path="verification/verified_login.png")
        print("Login Page screenshot saved.")

        # Verify Register Page
        print("Verifying Register Page...")
        page.goto(f"file://{os.getcwd()}/public/register.html")
        page.screenshot(path="verification/verified_register.png")
        print("Register Page screenshot saved.")

        # Verify Forgot Password Page
        print("Verifying Forgot Password Page...")
        page.goto(f"file://{os.getcwd()}/public/forgot-password.html")
        page.screenshot(path="verification/verified_forgot_password.png")
        print("Forgot Password Page screenshot saved.")

        # Verify Components Page (Fancy Table & Cards)
        print("Verifying Components Page...")
        page.goto(f"file://{os.getcwd()}/public/components.html")
        # Scroll down to see new components
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.screenshot(path="verification/verified_components_full.png", full_page=True)
        print("Components Page screenshot saved.")

        browser.close()

if __name__ == "__main__":
    run()
