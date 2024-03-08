from selenium import webdriver
import pytest


@pytest.fixture()
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
