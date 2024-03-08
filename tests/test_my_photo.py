from pages.phototime_pro.auth_user import AuthUser
from pages.phototime_pro.my_photo import MyPhoto
from locators.locators import Urls
import allure


class TestMyPhoto:
    # тест будет корректно отрабатывать, если будет куплено хотя бы
    # одно фото

    @allure.title('Позитивный тест - Проверка скачивания ранее приобретенного фото')
    def test_download_my_photo(self, driver):
        auth_user = AuthUser(driver)
        my_photo = MyPhoto(driver)
        auth_user.go_to_site(Urls.phototime_pro)
        auth_user.login_user()
        assert my_photo.download_photo() == "complete"
