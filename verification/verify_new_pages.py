
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the gallery file
        cwd = os.getcwd()
        gallery_url = f"file://{cwd}/public/gallery.html"
        admin_url = f"file://{cwd}/public/admin.html"

        print(f"Navigating to Gallery: {gallery_url}")
        page.goto(gallery_url)
        page.screenshot(path="verification/verified_gallery.png")
        print("Gallery screenshot saved.")

        # Test Lightbox (Click first item)
        # Note: Transitions take time, so we wait a bit
        page.locator(".gallery-item").first.click()
        page.wait_for_timeout(1000) # Wait for modal to open
        page.screenshot(path="verification/verified_gallery_lightbox.png")
        print("Gallery Lightbox screenshot saved.")

        print(f"Navigating to Admin: {admin_url}")
        page.goto(admin_url)
        page.screenshot(path="verification/verified_admin.png")
        print("Admin screenshot saved.")

        # Test Sidebar Mobile Toggle (emulate mobile)
        page.set_viewport_size({"width": 375, "height": 812})
        page.reload()
        page.wait_for_timeout(500)
        page.locator("#sidebarToggle").click()
        page.wait_for_timeout(500) # Wait for sidebar slide
        page.screenshot(path="verification/verified_admin_mobile_sidebar.png")
        print("Admin Mobile Sidebar screenshot saved.")

        browser.close()

if __name__ == "__main__":
    run()
