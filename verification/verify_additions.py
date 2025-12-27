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

        # Verify Doodles Page
        doodles_path = os.path.abspath("public/doodles.html")
        page.goto(f"file://{doodles_path}")
        page.screenshot(path="verification/verified_doodles.png", full_page=True)
        print("Verified doodles.html")

        # Verify Carousel Page
        carousel_path = os.path.abspath("public/carousel.html")
        page.goto(f"file://{carousel_path}")
        page.screenshot(path="verification/verified_carousel.png", full_page=True)
        print("Verified carousel.html")

        # Verify Cheatsheet Page
        cheatsheet_path = os.path.abspath("public/cheatsheet.html")
        page.goto(f"file://{cheatsheet_path}")
        page.screenshot(path="verification/verified_cheatsheet.png", full_page=True)
        print("Verified cheatsheet.html")

        # Verify Masonry Page
        masonry_path = os.path.abspath("public/masonry.html")
        page.goto(f"file://{masonry_path}")
        page.screenshot(path="verification/verified_masonry.png", full_page=True)
        print("Verified masonry.html")

        browser.close()

if __name__ == "__main__":
    verify_additions()
