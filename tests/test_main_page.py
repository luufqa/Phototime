from pages.phototime_pro.main_page import MainPage
from locators.locators import Urls
import allure


class TestMainPage:
    @allure.title('Позитивный тест - Проверка открытия ресурса get.phototime.pro')
    def test_partnership(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(Urls.phototime_pro)
        main_page.partnership()
        main_page.switch_window()
        assert main_page.current_url() == 'https://get.phototime.pro/'

    @allure.title('Позитивный тест - Проверка перехода через "Из мира фотографии"')
    def test_photo_news(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(Urls.phototime_pro)
        main_page.photo_news()
        assert main_page.current_url() == 'https://phototime.pro/'

    @allure.title('Позитивный тест - Проверка открытия Политики конфиденциальности')
    def test_politic(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(Urls.phototime_pro)
        main_page.politic()
        main_page.switch_window()
        assert main_page.current_url() == 'https://phototime.pro/license'

    @allure.title('Позитивный тест - Проверка открытия Политики конфиденциальности через форму авторизации')
    def test_politic_in_auth_form(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(Urls.phototime_pro)
        main_page.politic_in_auth_form()
        main_page.switch_window()
        assert main_page.current_url() == 'https://phototime.pro/license'

    @allure.title('Позитивный тест - Проверка <title>')
    def test_get_title_html(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(Urls.phototime_pro)
        assert main_page.get_title_html() == 'Phototime – фотоуслуги для развлекательного бизнеса'
