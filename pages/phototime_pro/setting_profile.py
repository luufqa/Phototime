from locators.locators import Setting
from pages.base_page import BasePage
import allure

class SettingProfile(BasePage):
    @allure.step('Переход в настройки пользователя')
    def setting_profile(self):
        self.find_element_located_click(Setting.setting_navi_button)
        self.find_element_located_click(Setting.accept_setting)
        notification = self.find_element_to_be_clickable(Setting.setting_changes_complete).text
        return notification
