"""
Sample Playwright test for buttons/links on https://playwright.dev/

Setup (run once):
    pip install playwright
    playwright install chromium

Run:
    python test_playwright_site.py
"""

from playwright.sync_api import sync_playwright, expect


def test_get_started_button(page):
    """Homepage 'Get started' button should navigate to the docs intro page."""
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    page.wait_for_url("**/docs/intro")
    expect(page).to_have_url(lambda url: "/docs/intro" in url)
    print("✔ 'Get started' button navigates to docs intro page")


def test_navbar_docs_link(page):
    """Top navbar 'Docs' link should load a documentation page."""
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Docs", exact=True).click()
    page.wait_for_url("**/docs/**")
    expect(page.locator("article")).to_be_visible()
    print("✔ Navbar 'Docs' link loads a docs page")


def test_navbar_api_link(page):
    """Top navbar 'API' link should load the API reference page."""
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="API", exact=True).click()
    page.wait_for_url("**/docs/api/**")
    expect(page).to_have_url(lambda url: "/docs/api" in url)
    print("✔ Navbar 'API' link loads the API reference page")


def test_search_button_opens_dialog(page):
    """Clicking the search button/icon should open the search modal."""
    page.goto("https://playwright.dev/")
    page.get_by_role("button", name="Search").click()
    search_dialog = page.get_by_placeholder("Search docs")
    expect(search_dialog).to_be_visible()
    print("✔ Search button opens the search dialog")
    page.keyboard.press("Escape")  # close it again


def test_theme_toggle_button(page):
    """Dark/light mode toggle button should switch the page's color theme."""
    page.goto("https://playwright.dev/")
    html = page.locator("html")
    theme_before = html.get_attribute("data-theme")

    toggle = page.get_by_role("button", name="Switch between dark and light mode")
    toggle.click()

    theme_after = html.get_attribute("data-theme")
    assert theme_before != theme_after, "Expected theme to change after clicking toggle"
    print(f"✔ Theme toggle button switched theme: {theme_before} -> {theme_after}")


def test_github_link_button(page, context):
    """GitHub icon/link in navbar should open the Playwright GitHub repo in a new tab."""
    page.goto("https://playwright.dev/")

    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="GitHub repository").click()
    github_page = new_page_info.value
    github_page.wait_for_load_state()
    expect(github_page).to_have_url(lambda url: "github.com/microsoft/playwright" in url)
    print("✔ GitHub link button opens the correct repository in a new tab")
    github_page.close()


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        tests = [
            lambda: test_get_started_button(page),
            lambda: test_navbar_docs_link(page),
            lambda: test_navbar_api_link(page),
            lambda: test_search_button_opens_dialog(page),
            lambda: test_theme_toggle_button(page),
            lambda: test_github_link_button(page, context),
        ]

        passed, failed = 0, 0
        for test in tests:
            try:
                test()
                passed += 1
            except Exception as e:
                failed += 1
                print(f"✘ Test failed: {e}")

        context.close()
        browser.close()

    print(f"\n{passed} passed, {failed} failed")


if __name__ == "__main__":
    main()