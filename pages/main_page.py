import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import AccordionData

class MainPage(BasePage):
    @allure.step("Клик по кнопке Да все привыкли")
    def click_on_button_cookie(self):
        self.click_on_element(MainPageLocators.COOKIE_BTN)

    @allure.step('Скролл до центра страницы')
    def scroll_to_center_page(self):
        self.scroll_to_element(MainPageLocators.FA_QUESTIONS)

    @allure.step('Скролл до конца страницы')
    def scroll_to_bottom_page(self):
        self.scroll_to_bottom()

    @allure.step('Ожидание появления заголовка Вопросы о важном')
    def wait_visibility_header_questions(self):
        self.wait_for_element(MainPageLocators.FA_QUESTIONS)

    @allure.step("Клик по заголовку аккордеона")
    def click_heading(self, heading_id):
        self.click_on_element(MainPageLocators.accordion_heading_by_id(heading_id))

    @allure.step("Получение текста вопроса")
    def get_heading_text(self, heading_id):
        return self.get_text_on_element(MainPageLocators.accordion_heading_by_id(heading_id))

    @allure.step("Получение текста раскрытого ответа")
    def get_panel_text(self, panel_id):
        return self.get_text_on_element(MainPageLocators.accordion_panel_by_id(panel_id))
