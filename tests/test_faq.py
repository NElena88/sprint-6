import allure
import pytest
from data import AccordionData
from pages.base_page import BasePage
from pages.main_page import MainPage

class TestFAQ:
    @allure.title("Тест выпадающего списка на соответствие текста")
    @pytest.mark.parametrize("heading_id, panel_id, expected_heading_text, expected_panel_text",
                             AccordionData.panel_data)
    def test_faq_heading_and_panel(self, driver, heading_id, panel_id, expected_heading_text, expected_panel_text):
        main_page = MainPage(driver)
        main_page.click_on_button_cookie()
        main_page.scroll_to_bottom_page()
        actual_heading_text = main_page.get_heading_text(heading_id)
        assert actual_heading_text == expected_heading_text, f"Ожидался текст вопроса: {expected_heading_text}, но был: {actual_heading_text}"

        main_page.click_heading(heading_id)

        actual_panel_text = main_page.get_panel_text(panel_id)
        assert actual_panel_text == expected_panel_text, f"Ожидался текст ответа: {expected_panel_text}, но был: {actual_panel_text}"
