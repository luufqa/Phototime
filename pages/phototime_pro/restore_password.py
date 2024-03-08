from locators.locators import Account
from pages.base_page import BasePage
from locators.locators import Auth
import allure


class RestorePassword(BasePage):
    @allure.step('Восстановление пароля - отправка СМС на номер')
    def restore_password(self):
        self.find_element_located_click(Auth.login_button)
        self.find_element_located_click(Auth.restore_button)
        self.find_element_all_located(Auth.restore_phone_field)[1].send_keys(Account.phone)
        self.find_element_located_click(Auth.restore_send_password)
        notification = self.find_element_to_be_clickable(Auth.restore_password_complete).text
        return notification
