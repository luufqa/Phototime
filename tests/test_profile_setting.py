from pages.phototime_pro.setting_profile import SettingProfile
from pages.phototime_pro.auth_user import AuthUser
from locators.locators import Urls
import allure


class TestProfileSetting:

    @allure.title('Позитивный тест - Проверка перехода в Настройки профиля и сверка данных')
    def test_profile_setting(self, driver):
        auth_user = AuthUser(driver)
        setting_profile = SettingProfile(driver)
        auth_user.go_to_site(Urls.phototime_pro)
        auth_user.login_user()
        notification = setting_profile.setting_profile()
        assert notification == 'Настройки изменены'
