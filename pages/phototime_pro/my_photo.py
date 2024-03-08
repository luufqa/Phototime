from pages.base_page import BasePage
from locators.locators import Photo
import getpass
import shutil
import allure
import time
import os


class MyPhoto(BasePage):
    @allure.step('Скачивание файла и проверка его наличие в папке Загрузки')
    def download_photo(self):
        current_user = getpass.getuser()
        download_directory = f"/Users/{current_user}/Downloads"
        # Можно реализовать функцию очистки директории - перед скачиванием файла
        # try:
        #     shutil.rmtree(download_directory)
        # except PermissionError:
        #     pass
        self.find_element_all_located(Photo.download_button)[1].click()
        # Ждем некоторое время, чтобы скачивание началось или завершилось
        time.sleep(5)
        # Проверяем, что файл загружен в папку "Загрузки"
        files = os.listdir(download_directory)
        if any("image.jpeg" in file for file in files):
            return 'complete'
        else:
            return 'file is not found'
