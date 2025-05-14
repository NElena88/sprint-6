import allure
import pytest

from helpers import generate_personal_information
from pages import order_page
from curl import main_site
from locators.order_locators import OrderLocators
from pages.order_page import OrderPage
from data import test_personal_info_data


class TestOrder:

    @pytest.mark.parametrize("name, lastname, address, station, phone", test_personal_info_data)
    @allure.title("Тест заказа аренды самоката и переход на главную страницу")
    def test_input_personal_information(self, driver, name, lastname, address, station, phone):
        order_page = OrderPage(driver)
        order_page.click_on_button_cookie()
        order_page.click_order_button()

        order_page.fill_form_personal_information(name, lastname, address, station, phone)
        order_page.click_submit_order()
        order_page.wait_visibility_header_rental()

        assert order_page.get_text_element_header_rental() == "Про аренду"

        order_page.click_rental_date()
        order_page.wait_visibility_rental_date()
        order_page.click_select_rental_date()
        order_page.click_open_dropdown()
        order_page.wait_visibility_dropdown()
        order_page.click_selected_dropdown_value()
        order_page.click_selected_color_scooter()
        order_page.click_field_comment_leave_a_comment()

        order_page.wait_clickable_button_order()
        order_page.click_confirm_the_order()

        order_page.wait_for_order_popup()
        order_page.wait_clickable_button_yes()
        order_page.click_on_button_confirm_the_order_yes()

        order_page.wait_order_confirmed_popup()
        header_text = order_page.get_text_on_header_order_confirmed()
        assert "Заказ оформлен" in header_text

        order_page.wait_clickable_button_view_status()
        order_page.click_on_button_view_status()
        order_page.wait_for_clickable_logo_samokat()
        order_page.click_on_logo_samokat()

        order_page.wait_for_main_page()
        main_text = order_page.get_text_on_header_main_page()
        assert "Самокат" in main_text

        order_page.click_on_logo_yandex()
        dzen_url = order_page.switch_and_get_url_dzen()
        assert "dzen.ru" in dzen_url









