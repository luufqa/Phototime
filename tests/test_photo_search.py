from pages.phototime_pro.search_photo import SearchPhoto
from pages.phototime_pro.auth_user import AuthUser
from locators.locators import Urls
import allure


class TestSearchPhoto:

    @allure.title('Позитивный тест - Проверка функции поиска фото/оплата/удаление из корзины')
    def test_search_photo(self, driver):
        auth_user = AuthUser(driver)
        search = SearchPhoto(driver)
        auth_user.go_to_site(Urls.phototime_pro)
        auth_user.login_user()
        result = search.search_photo()
        assert 'Список пуст' in result
