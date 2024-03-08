from pages.base_page import BasePage
from locators.locators import Auth
from locators.locators import Main
from bs4 import BeautifulSoup
import requests
import allure


class MainPage(BasePage):
    @allure.step('Открытие страницы "Сотрудничество" get.phototime.pro')
    def partnership(self):
        self.find_element_all_located(Main.partnership)[1].click()

    @allure.step('Открытие страницы "Из мира фотографии"')
    def photo_news(self):
        self.find_element_all_located(Main.photo_news)[0].click()
        self.find_element_all_located(Main.photo_news)[0].click()

    @allure.step('Открытие Политики конфиденциальности')
    def politic(self):
        self.find_element_located_click(Main.politic_info)

    @allure.step('Открытие Политики конфиденциальности через форму авторизации')
    def politic_in_auth_form(self):
        self.find_element_located_click(Auth.login_button)
        self.find_element_located_click(Main.rules_in_auth_form)

    @allure.step('Получение значения <title>')
    def get_title_html(self):
        response = requests.get(self.current_url())
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        return title
