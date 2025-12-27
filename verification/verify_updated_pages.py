from playwright.sync_api import sync_playwright
import os

def verify_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()

        # Define pages to test
        pages = [
            'backgrounds.html',
            'documentation.html',
            '404.html',
            'index.html',
            'blog.html'
        ]

        # Ensure screenshot dir exists
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')

        for page_file in pages:
            file_path = f"file://{os.path.abspath(f'public/{page_file}')}"
            print(f"Verifying {page_file}...")

            try:
                page.goto(file_path)
                page.screenshot(path=f"screenshots/{page_file.replace('.html', '.png')}", full_page=True)
                print(f"{page_file} screenshot saved.")
            except Exception as e:
                print(f"Error verifying {page_file}: {e}")

        browser.close()

if __name__ == "__main__":
    verify_pages()
