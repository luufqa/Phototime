from locators.locators import Payment
from pages.base_page import BasePage
from locators.locators import Search
from locators.locators import Cart
import allure


class SearchPhoto(BasePage):
    @allure.step('Поиск фото, переход к форме оплаты, удаление из корзины')
    def search_photo(self):
        self.find_element_located_click(Search.search_navi_button)
        self.find_element_located_click(Search.accept_search)
        self.find_element_located_click(Search.search_field)
        self.find_element_located_click(Search.first_location)
        self.find_element_located_click(Search.accept_search)
        self.find_element_to_be_clickable(Search.first_photo)
        self.find_element_located_click(Search.cart_photo)
        self.find_element_located_click(Search.cart_in_search)
        self.find_element_located_click(Cart.buy_button)
        self.find_element_located_click(Payment.bank_card)
        self.find_element_located_click(Payment.logout_bank_card)
        self.find_element_located_click(Payment.close_payment_modal)
        self.find_element_located_click(Cart.cart_navi_button)
        cart = self.find_element_to_be_clickable(Search.cart_photo)
        cart.click()
        result = self.find_element_located(Cart.cart_list).text
        return result
