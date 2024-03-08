from pages.phototime_pro.auth_user import AuthUser
from locators.locators import Urls
import allure


class TestAuthUser:

    @allure.title('Позитивный тест - Авторизация пользователя')
    def test_login_user(self, driver):
        auth_user = AuthUser(driver)
        auth_user.go_to_site(Urls.phototime_pro)
        auth_user.login_user()
        assert auth_user.current_url() == "https://phototime.pro/photo"

    @allure.title('Позитивный тест - Авторизация пользователя через меню Регистрация')
    def test_login_user_in_reg(self, driver):
        auth_user = AuthUser(driver)
        auth_user.go_to_site(Urls.phototime_pro)
        auth_user.login_user_in_reg()
        assert auth_user.current_url() == "https://phototime.pro/photo"

    @allure.title('Позитивный тест - Выход из аккаунта')
    def test_logout_user(self, driver):
        auth_user = AuthUser(driver)
        auth_user.go_to_site(Urls.phototime_pro)
        auth_user.login_user()
        auth_user.logout_user()

        assert auth_user.current_url() == 'https://phototime.pro/'
