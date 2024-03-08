from pages.phototime_pro.restore_password import RestorePassword
from locators.locators import Urls
import allure


class TestRestorePassword:
    # пароль будет сбрасываться после выполнения test_restore_password
    # возможно, вам потребуется создать свою учетку и подставить данные
    @allure.title('Позитивный тест - Проверка восстановления пароля с отправкой СМС на номер')
    def test_restore_password(self, driver):
        restore_password = RestorePassword(driver)
        restore_password.go_to_site(Urls.phototime_pro)
        notification = restore_password.restore_password()
        assert notification == 'Новый пароль отправлен по SMS'
