from locators.locators import Account
from pages.base_page import BasePage
from locators.locators import Auth
from locators.locators import Cart
from locators.locators import Reg
import allure


class AuthUser(BasePage):
    @allure.step('Переход в форму авторизации')
    def login_user(self):
        self.find_element_located_click(Auth.login_button)
        self.find_element_to_be_clickable(Auth.phone_field).send_keys(Account.phone)
        self.find_element_to_be_clickable(Auth.password_field).send_keys(Account.password)
        self.find_element_to_be_clickable(Auth.accept_login)
        self.find_element_located_click(Auth.accept_login)
        self.find_element_to_be_clickable(Cart.cart_navi_button)

    @allure.step('Переход в форму авторизации через кнопку Регистрация')
    def login_user_in_reg(self):
        self.find_element_located_click(Auth.login_button)
        self.find_element_located_click(Reg.reg_button)
        self.find_element_located_click(Reg.login_button_in_reg)
        self.find_element_to_be_clickable(Auth.phone_field).send_keys(Account.phone)
        self.find_element_to_be_clickable(Auth.password_field).send_keys(Account.password)
        self.find_element_to_be_clickable(Auth.accept_login)
        self.find_element_located_click(Auth.accept_login)
        self.find_element_to_be_clickable(Cart.cart_navi_button)

    @allure.step('Выход из аккаунта')
    def logout_user(self):
        self.find_element_to_be_clickable(Auth.logout_button)
        self.find_element_located_click(Auth.logout_button)
