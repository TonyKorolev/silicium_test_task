from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pathlib import Path
from .base_page import BasePage
from .locators import PracticeFormLocators as Locators


class PracticeForm(BasePage):

    def fill_first_name(self, first_name: str) -> None:
        first_name_input = self.browser.find_element(*Locators.FIRST_NAME_INPUT)
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def fill_last_name(self, last_name: str) -> None:
        last_name_input = self.browser.find_element(*Locators.LAST_NAME_INPUT)
        last_name_input.clear()
        last_name_input.send_keys(last_name)

    def fill_email(self, email: str) -> None:
        email_input = self.browser.find_element(*Locators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def select_gender(self, gender: str) -> None:
        button = None
        match gender:
            case 'Male':
                button = self.browser.find_element(*Locators.MALE_GENDER_RADIOBUTTON)
            case 'Female':
                button = self.browser.find_element(*Locators.FEMALE_GENDER_RADIOBUTTON)
            case 'Other':
                button = self.browser.find_element(*Locators.OTHER_GENDER_RADIOBUTTON)
        button.click()

    def fill_mobile_number(self, number: str) -> None:
        mobile_number_input = self.browser.find_element(*Locators.MOBILE_NUMBER)
        mobile_number_input.clear()
        mobile_number_input.send_keys(number)

    def fill_date_of_birth(self, date: str, month: str, year: str) -> None:
        self.browser.find_element(*Locators.DATE_OF_BIRTH_INPUT).click()
        month_select = Select(self.browser.find_element(*Locators.MONTH_COMBOBOX))
        month_select.select_by_visible_text(month)
        year_select = Select(self.browser.find_element(*Locators.YEAR_COMBOBOX))
        year_select.select_by_visible_text(year)
        self.browser.find_element(By.XPATH, Locators.date_of_birth(date)).click()

    def fill_subjects(self, subjects: str) -> None:
        self.browser.find_element(*Locators.SUBJECTS).click()
        self.browser.find_element(*Locators.SUBJECTS_INPUT).send_keys(subjects)

    def upload_picture(self, file_name):
        self.browser.find_element(*Locators.UPLOAD_PICTURE_INPUT).send_keys(str(Path.cwd() / file_name))

    def fill_current_address(self, address: str) -> None:
        current_address_input = self.browser.find_element(*Locators.CURRENT_ADDRESS)
        current_address_input.clear()
        current_address_input.send_keys(address)

    def select_state(self, state: str) -> None:
        # state_select = Select(self.browser.find_element(*Locators.STATE_COMBOBOX))
        # state_select.select_by_visible_text(state)
        self.browser.find_element(*Locators.STATE_COMBOBOX).click()
        self.browser.find_element(*Locators.HARYANA).click()

    def select_city(self, city: str) -> None:
        # city_select = Select(self.browser.find_element(*Locators.CITY_COMBOBOX))
        # city_select.select_by_visible_text(city)
        self.browser.find_element(*Locators.CITY_COMBOBOX).click()
        self.browser.find_element(*Locators.KARNAL).click()

    def is_city_combobox_disabled(self) -> bool:
        return self.is_element_disabled(*Locators.CITY_COMBOBOX_INPUT)

    def submit_click(self) -> None:
        return self.browser.find_element(*Locators.SUBMIT_BUTTON).click()

    def is_modal_window_visible(self) -> bool:
        return self.is_element_visible(*Locators.MODAL_WINDOW)

    def is_thank_message_visible(self) -> bool:
        return self.is_element_visible(*Locators.THANK_MESSAGE)
