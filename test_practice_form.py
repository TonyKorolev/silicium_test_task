from .pages.practice_form import PracticeForm


def test_practice_form(browser):
    url = 'https://demoqa.com/automation-practice-form'
    page = PracticeForm(browser, url, timeout=1)
    page.open()
    page.fill_first_name('Tony')
    page.fill_last_name('Simba')
    page.fill_email('ololosh@mail.ru')
    page.select_gender('Male')
    page.fill_mobile_number('9171234567')
    page.fill_date_of_birth(date='28', month='August', year='1992')
    browser.implicitly_wait(10)
    page.fill_subjects('Subjects')
    page.upload_picture('img.png')
    page.fill_current_address('Lenina street, 32/1-3')
    assert page.is_city_combobox_disabled(), 'City combobox is enabled, should be disabled'
    page.select_state('Haryana')
    page.select_city('Karnal')
    page.submit_click()
    assert page.is_modal_window_visible(), 'Modal window is absent'
    assert page.is_thank_message_visible(), 'No thank message'

