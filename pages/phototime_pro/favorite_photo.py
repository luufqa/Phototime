from locators.locators import Favorite
from pages.base_page import BasePage
from locators.locators import Search
import allure


class FavoritePhoto(BasePage):
    @allure.step('Добавление и удаление фото из Избранного')
    def favorite_photo(self):
        self.find_element_located_click(Search.search_navi_button)
        self.find_element_located_click(Search.accept_search)
        self.find_element_located_click(Search.search_field)
        self.find_element_located_click(Search.first_location)
        self.find_element_located_click(Search.accept_search)
        self.find_element_to_be_clickable(Search.first_photo)
        self.find_element_located_click(Favorite.favorite_add_photo)
        notification = self.find_element_to_be_clickable(Favorite.favorite_notification).text
        self.find_element_located_click(Favorite.favorite)
        self.driver.refresh()
        self.find_element_located_click(Favorite.favorite_add_photo)
        result = self.find_element_to_be_clickable(Favorite.favorite_empty).text
        return result, notification
