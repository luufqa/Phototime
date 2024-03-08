from locators.locators import Contacts
from pages.base_page import BasePage
import allure


class ContactProfile(BasePage):
    @allure.step('Сохранение всех ключевых данных в список')
    def contact_profile(self):
        self.find_element_located_click(Contacts.contacts)
        data = []
        strings = self.find_element_all_located(Contacts.contacts_keys_elements)
        for i in strings:
            data.append(i.text)
        return data
