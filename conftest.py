import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils import perform_login


@pytest.fixture
def driver():
    """Inicia una instancia de Chrome configurada para las pruebas automatizadas."""
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    yield browser
    browser.quit()


@pytest.fixture
def login_in_driver(driver):
    perform_login(driver)
    return driver
