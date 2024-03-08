from pages.phototime_pro.contact_profile import ContactProfile
from pages.phototime_pro.auth_user import AuthUser
from locators.locators import Contacts
from locators.locators import Urls
import allure


class TestContactProfile:

    @allure.title('Позитивный тест - Проверка соответствия данных в разделе Контакты')
    def test_contact_profile(self, driver):
        auth_user = AuthUser(driver)
        contacts = ContactProfile(driver)
        auth_user.go_to_site(Urls.phototime_pro)
        auth_user.login_user()
        assert contacts.contact_profile() == Contacts.contacts_data
