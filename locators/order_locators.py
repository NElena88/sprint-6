from selenium.webdriver.common.by import By


class OrderLocators:
    COOKIE_BTN = (By.ID, "rcc-confirm-button")
    BUTTON_ORDER_TOP = (By.CSS_SELECTOR, "button.Button_Button__ra12g:not(.Button_Middle__1CSJM)")

    HEADER_ORDER_FOR_WHOM = (By.XPATH, "//div[@class='Order_Header__BZXOb' and text()='Для кого самокат']")

    INPUT_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    INPUT_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_STATION = (By.XPATH, "//li[@data-value={station}]")
    INPUT_PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    HEADER_ORDER_RENTAL = (By.XPATH, "//div[@class='Order_Header__BZXOb' and text()='Про аренду']")

    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    SELECT_DATE = (By.XPATH, '//div[@role="button" and @aria-label="Choose суббота, 24-е мая 2025 г."]')

    DROPDOWN_CONTROL = (By.CLASS_NAME, "Dropdown-arrow")
    OPTION_ONE_DAY = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    OPTION_TWO_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")

    CHOOSE_COLOR_BLACK = (By.ID, "black")
    CHOOSE_COLOR_GREY = (By.ID, "grey")
    INPUT_COMMENT = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
    BUTTON_ORDER_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and not(contains(@class, 'Button_Inverted__3IF-i')) and text()='Заказать']")

    MODAL_ORDER_POPUP = (By.CSS_SELECTOR, "div.Order_Modal__YZ-d3")
    BUTTON_ORDER_YES = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']//button[text()='Да']")

    MODAL_ORDER_CONFIRMED = (By.XPATH, '//div[@class="Order_Modal__YZ-d3" and .//div[contains(text(), "Заказ оформлен")]]')
    HEADER_ORDER_CONFIRMED = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ" and contains(.//text(), "Заказ оформлен")]')
    BUTTON_VIEW_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")

    LOGO_SAMOKAT = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    HEADER_MAIN_TEXT = (By.XPATH, "//div[contains(@class, 'Home_Header__') and contains(text(), 'Самокат')]")

    @staticmethod
    def station_suggestion(station):
        return ((By.XPATH, f"//button[contains(@class, 'select-search__option')]//div[text()='{station}']"))

