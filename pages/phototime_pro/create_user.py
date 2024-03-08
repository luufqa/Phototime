from locators.locators import Account
from pages.base_page import BasePage
from locators.locators import Auth
from locators.locators import Reg
import allure


class CreateUser(BasePage):
    @allure.step('Создание нового пользователя с темже номером')
    def create_user_with_double_phone(self):
        self.find_element_located_click(Auth.login_button)
        self.find_element_located_click(Reg.reg_button)
        self.find_element_all_located(Reg.first_name_user)[0].send_keys(Account.first_name)
        self.find_element_all_located(Reg.last_name_user)[1].send_keys(Account.last_name)
        self.find_element_all_located(Reg.phone_number_user)[2].send_keys(Account.phone)
        self.find_element_all_located(Reg.email_user)[3].send_keys(Account.email)
        self.find_element_located(Reg.password_user).send_keys(Account.password)
        self.find_element_located_click(Reg.enable_visible_password)
        self.find_element_located_click(Reg.accept_reg_button)
        notification = self.find_element_to_be_clickable(Reg.error_alert_reg).text
        return notification
