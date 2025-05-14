from selenium.webdriver.common.by import By
from data import AccordionData


class MainPageLocators:
    COOKIE_BTN = (By.ID, "rcc-confirm-button")
    FA_QUESTIONS = (By.CSS_SELECTOR, "div.Home_SubHeader__zwi_E")
    BUTTON_ORDER_TOP = (By.CSS_SELECTOR, "button.Button_Button__ra12g:not(.Button_Middle__1CSJM)")
    BUTTON_ORDER_BOTTOM = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")

    @staticmethod
    def accordion_heading_by_id(heading_id):
         return (By.ID, heading_id)

    @staticmethod
    def accordion_panel_by_id(panel_id):
        return (By.ID, panel_id)
