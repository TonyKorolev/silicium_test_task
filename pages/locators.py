from selenium.webdriver.common.by import By


class PracticeFormLocators:
    FIRST_NAME_INPUT = (By.ID, 'firstName')
    LAST_NAME_INPUT = (By.ID, 'lastName')
    EMAIL_INPUT = (By.ID, 'userEmail')
    MALE_GENDER_RADIOBUTTON = (By.XPATH, '//input[@id="gender-radio-1"]/parent::div')
    FEMALE_GENDER_RADIOBUTTON = (By.XPATH, '//input[@id="gender-radio-2"]/parent::div')
    OTHER_GENDER_RADIOBUTTON = (By.XPATH, '//input[@id="gender-radio-3"]/parent::div')
    MOBILE_NUMBER = (By.CSS_SELECTOR, '#userNumber')
    DATE_OF_BIRTH_INPUT = (By.ID, 'dateOfBirthInput')
    MONTH_COMBOBOX = (By.XPATH, '//*[contains(@class, "react-datepicker__month-select")]')
    YEAR_COMBOBOX = (By.XPATH, '//*[contains(@class, "react-datepicker__year-select")]')
    SUBJECTS = (By.XPATH, '//div[contains(@class, "subjects-auto-complete__value-container")]')
    SUBJECTS_INPUT = (By.XPATH, '//div[contains(@class, "subjects-auto-complete__value-container")]//input')
    UPLOAD_PICTURE_INPUT = (By.ID, 'uploadPicture')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@class="form-control"]')
    STATE_COMBOBOX = (By.XPATH, '//*[text()="Select State"]')
    HARYANA = (By.XPATH, '//*[text()="Haryana"]')
    CITY_COMBOBOX = (By.XPATH, '//*[text()="Select City"]')
    KARNAL = (By.XPATH, '//*[text()="Karnal"]')
    CITY_COMBOBOX_INPUT = (By.XPATH, '//div[@id="city"]//input')
    SUBMIT_BUTTON = (By.ID, 'submit')
    MODAL_WINDOW = (By.XPATH, '//div[@class="modal-content"]')
    THANK_MESSAGE = (By.XPATH, '//*[text()="Thanks for submitting the form"]')

    @staticmethod
    def date_of_birth(date: str) -> str:
        return (f'//div[contains(@class, "react-datepicker__day") and not(contains(@class, "outside-month")) '
                f'and text()={date}]')
