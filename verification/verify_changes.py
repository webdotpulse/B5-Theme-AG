import os
from playwright.sync_api import sync_playwright, expect

def verify_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # 1. Verify Index Page Header Image
        index_path = os.path.abspath("public/index.html")
        page.goto(f"file://{index_path}")

        # Check title
        expect(page).to_have_title("About Me | Arsela Gjonaj")

        # Check navbar logo
        expect(page.locator(".navbar-brand")).to_have_text("Arsela Gjonaj")

        # Check for the new image source
        header_image = page.locator("header img")
        expect(header_image).to_be_visible()
        # Verify the src attribute ends with arsi.png
        # Note: file:// protocol might make the src absolute, so we check if it contains the filename
        src = header_image.get_attribute("src")
        assert "arsi.png" in src, f"Expected header image src to contain 'arsi.png', but got '{src}'"

        # Take screenshot of the header
        header = page.locator("header")
        header.screenshot(path="verification/index_header.png")
        print("Verified index.html header image and generated verification/index_header.png")

        # 2. Verify Blog Post Page
        blog_post_path = os.path.abspath("public/blog-post.html")
        page.goto(f"file://{blog_post_path}")

        # Check title
        expect(page).to_have_title("Understanding Color Theory | Arsela Gjonaj")

        # Check content existence
        expect(page.locator("h1")).to_have_text("Understanding Color Theory")
        expect(page.locator("article")).to_be_visible()

        # Check sidebar existence
        expect(page.locator("aside")).to_be_visible()

        # Take screenshot of the full page
        page.screenshot(path="verification/blog_post.png", full_page=True)
        print("Verified blog-post.html content and generated verification/blog_post.png")

        browser.close()

if __name__ == "__main__":
    verify_changes()
