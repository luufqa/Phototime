from pages.phototime_pro.favorite_photo import FavoritePhoto
from pages.phototime_pro.auth_user import AuthUser
from locators.locators import Urls
import allure


class TestFavoritePhoto:

    @allure.title('Позитивный тест - Проверка добавления фото и удаление из Избранного')
    def test_favorite_photo(self, driver):
        auth_user = AuthUser(driver)
        favorite = FavoritePhoto(driver)
        auth_user.go_to_site(Urls.phototime_pro)
        auth_user.login_user()
        result, notification = favorite.favorite_photo()
        assert result == "- Список пуст -"
        assert notification == "Фотография добалена в избранное"
