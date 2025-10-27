from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_inventory_shows_selected_product(login_in_driver):
    driver = login_in_driver

    assert driver.title == "Swag Labs"

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert products, "No hay productos visibles en la vista de inventario"

    # Añade el primer producto disponible al carrito para validar el flujo básico.
    products[0].find_element(By.TAG_NAME, "button").click()

    wait = WebDriverWait(driver, 10)
    badge = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == "1", f"El contador del carrito debería mostrar 1, pero muestra {badge.text}"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_item = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))
    assert cart_item.is_displayed(), "El producto añadido no se encuentra en el carrito"
