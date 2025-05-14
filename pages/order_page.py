import allure

from pages.base_page import BasePage
from locators.order_locators import OrderLocators
from helpers import generate_personal_information
from helpers import AddressGenerator


class OrderPage(BasePage):
    @allure.step("Клик по кнопке Да все привыкли")
    def click_on_button_cookie(self):
        self.click_on_element(OrderLocators.COOKIE_BTN)

    @allure.step("Нажать на кнопку Заказать")
    def click_order_button(self):
        self.click_on_element(OrderLocators.BUTTON_ORDER_TOP)

    @allure.step("Заполнить форму личных данных")
    def fill_form_personal_information(self, name, lastname, address, station, phone):
        self.send_keys_to_input(OrderLocators.INPUT_NAME, name)
        self.send_keys_to_input(OrderLocators.INPUT_LASTNAME, lastname)
        self.send_keys_to_input(OrderLocators.INPUT_ADDRESS, address)
        self.send_keys_to_input(OrderLocators.INPUT_STATION_FIELD, station)
        self.wait_for_element(OrderLocators.station_suggestion(station))
        self.click_on_element(OrderLocators.station_suggestion(station))
        self.send_keys_to_input(OrderLocators.INPUT_PHONE, phone)

    @allure.step("Подтвердить кнопку заказа")
    def click_submit_order(self):
        self.click_on_element(OrderLocators.NEXT_BUTTON)

    @allure.step("Подождать видимости заголовка Про аренду")
    def wait_visibility_header_rental(self):
        self.wait_for_element(OrderLocators.HEADER_ORDER_RENTAL)

    @allure.step("Получить текст заголовка Про аренду")
    def get_text_element_header_rental(self):
        return self.get_text_on_element(OrderLocators.HEADER_ORDER_RENTAL)

    @allure.step("Нажать на поле Когда привезти самокат")
    def click_rental_date(self):
        self.click_on_element(OrderLocators.INPUT_DATE)

    @allure.step("Дождаться видимости выбранной даты")
    def wait_visibility_rental_date(self):
        self.wait_for_element(OrderLocators.SELECT_DATE)

    @allure.step("Выбрать дату")
    def click_select_rental_date(self):
        self.click_on_element(OrderLocators.SELECT_DATE)

    @allure.step("Открыть выпадающий список")
    def click_open_dropdown(self):
        self.click_on_element(OrderLocators.DROPDOWN_CONTROL)

    @allure.step("Дождаться видимости списка сроков аренды")
    def wait_visibility_dropdown(self):
        self.wait_for_element(OrderLocators.DROPDOWN_CONTROL)

    @allure.step('Выбрать срок аренды')
    def click_selected_dropdown_value(self):
        self.click_on_element(OrderLocators.OPTION_ONE_DAY)

    @allure.step('Выбрать цвет самоката')
    def click_selected_color_scooter(self):
        self.click_on_element(OrderLocators.CHOOSE_COLOR_BLACK)

    @allure.step('Оставить комментарий #')
    def click_field_comment_leave_a_comment(self):
        self.click_on_element(OrderLocators.INPUT_COMMENT)
        self.send_keys_to_input(OrderLocators.INPUT_COMMENT, "#")

    @allure.step("Подождать кликабельности кнопки Заказать")
    def wait_clickable_button_order(self):
        self.wait_for_clickable_element(OrderLocators.BUTTON_ORDER_BOTTOM)

    @allure.step('Подтвердить заказ кнопкой Заказать')
    def click_confirm_the_order(self):
        self.click_on_element(OrderLocators.BUTTON_ORDER_BOTTOM)

    @allure.step("Дождаться появления окна подтверждения заказа")
    def wait_for_order_popup(self):
        self.wait_for_element(OrderLocators.MODAL_ORDER_POPUP)

    @allure.step("Подождать кликабельности кнопки Да")
    def wait_clickable_button_yes(self):
        self.wait_for_clickable_element(OrderLocators.BUTTON_ORDER_YES)

    @allure.step('Подтвердить заказ кнопкой Да')
    def click_on_button_confirm_the_order_yes(self):
        self.click_on_element(OrderLocators.BUTTON_ORDER_YES)

    @allure.step('Дождаться появления окна Заказ оформлен')
    def wait_order_confirmed_popup(self):
        self.wait_for_element(OrderLocators.MODAL_ORDER_CONFIRMED)

    @allure.step("Получить текст заголовка Заказ оформлен")
    def get_text_on_header_order_confirmed(self):
        return self.get_text_on_element(OrderLocators.HEADER_ORDER_CONFIRMED)

    @allure.step("Подождать кликабельности кнопки Посмотреть статус")
    def wait_clickable_button_view_status(self):
        self.wait_for_clickable_element(OrderLocators.BUTTON_VIEW_STATUS)

    @allure.step('Нажать на кнопку Посмотреть статус')
    def click_on_button_view_status(self):
        self.click_on_element(OrderLocators.BUTTON_VIEW_STATUS)

    @allure.step('Дождаться кликабельности логотипа Самокат')
    def wait_for_clickable_logo_samokat(self):
        self.wait_for_clickable_element(OrderLocators.LOGO_SAMOKAT)

    @allure.step('Нажать на логотип Самокат')
    def click_on_logo_samokat(self):
        self.click_on_element(OrderLocators.LOGO_SAMOKAT)

    @allure.step("Дождаться появления главной страницы")
    def wait_for_main_page(self):
        self.wait_for_element(OrderLocators.HEADER_MAIN_TEXT)

    @allure.step("Получить текст заголовка главной страницы")
    def get_text_on_header_main_page(self):
        return self.get_text_on_element(OrderLocators.HEADER_MAIN_TEXT)

    @allure.step('Нажать на логотип Яндекс')
    def click_on_logo_yandex(self):
        self.click_on_element(OrderLocators.LOGO_YANDEX)

    @allure.step('Получить url Дзен.ру')
    def switch_and_get_url_dzen(self):
        return self.switch_and_get_url()