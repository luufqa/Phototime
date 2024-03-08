from pages.phototime_pro.create_user import CreateUser
from locators.locators import Urls
import allure


class TestCreateUser:

    @allure.title('Негативный тест - Невозможно создать пользователя с темже номер, который уже зарегистрирован')
    def test_create_user_with_double_phone(self, driver):
        create_user = CreateUser(driver)
        create_user.go_to_site(Urls.phototime_pro)
        notification = create_user.create_user_with_double_phone()
        assert notification == "Данный пользователь уже зарегистрирован!"
