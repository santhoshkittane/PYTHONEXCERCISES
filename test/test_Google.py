"""
Sample Playwright test for google.com

Setup (run once):
    pip install playwright
    playwright install chromium

Run:
    python test_google.py
"""

from playwright.sync_api import sync_playwright, expect


def test_google_homepage_loads(page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")
    print("✔ Homepage loaded and title is correct")


def test_google_search(page):
    page.goto("https://www.google.com")

    # Accept cookie consent dialog if it appears (common in EU/some regions)
    for label in ["Accept all", "I agree"]:
        try:
            page.get_by_role("button", name=label).click(timeout=3000)
            break
        except Exception:
            pass

    # Type a query into the search box and submit
    search_box = page.get_by_role("combobox", name="Search")
    search_box.click()
    search_box.fill("Playwright Python")
    search_box.press("Enter")

    # Wait for results page to load and verify results are shown
    page.wait_for_selector("#search")
    expect(page).to_have_title(lambda title: "Playwright Python" in title)
    results = page.locator("#search .g")
    assert results.count() > 0, "Expected at least one search result"
    print(f"✔ Search returned {results.count()} visible result blocks")


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        test_google_homepage_loads(page)
        test_google_search(page)

        browser.close()
    print("\nAll tests passed!")


if __name__ == "__main__":
    main()