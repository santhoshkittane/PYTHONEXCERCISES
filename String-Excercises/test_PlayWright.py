from playwright.sync_api import sync_playwright

def test():
    with test_sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:4200/')
        page.goto('http://localhost:4200/pages/iot-dashboard')
        page.get_by_role('link', name='Forms').click()
        page.get_by_role('link', name='Form Layouts').click()
        page.get_by_label('Email address').click()
        button = page.locator('nb-card').filter(has_text='Basic formEmail').get_by_role('button')
        assert button.is_visible()
        browser.close()