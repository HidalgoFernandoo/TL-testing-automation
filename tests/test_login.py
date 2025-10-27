
def test_login_redirects_to_inventory(login_in_driver):
    driver = login_in_driver

    # Confirma que el flujo de login aterriza en la página de inventario.
    assert "/inventory.html" in driver.current_url, "La redirección posterior al login es incorrecta"

    # El título confirma que la vista de inventario está activa.
    assert driver.title == "Swag Labs"
