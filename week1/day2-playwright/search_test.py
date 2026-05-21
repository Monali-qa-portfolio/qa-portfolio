from playwright.sync_api import sync_playwright

def test_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("Opening Wikipedia...")
        page.goto("https://www.wikipedia.org")

        print("Typing search query...")
        page.locator("input#searchInput").fill("QA Automation")
        page.locator("input#searchInput").press("Enter")

        page.wait_for_load_state("networkidle")

        title = page.title()
        print(f"Page title: {title}")

        if "automation" in title.lower() or "quality" in title.lower():
            print("[PASS] Search results loaded successfully")
        else:
            print(f"[FAIL] Unexpected page title: {title}")

        page.screenshot(path="search_results.png")
        print("[SCREENSHOT] Saved as search_results.png")
        browser.close()

test_search()