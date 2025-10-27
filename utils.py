from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def perform_login(driver, username="standard_user", password="secret_sauce"):
    """Ingresar a SauceDemo y autenticarse con las credenciales provistas."""
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    # Garantiza que la navegación hacia la página de inventario finalice antes de continuar.
    wait.until(EC.url_contains("/inventory"))
