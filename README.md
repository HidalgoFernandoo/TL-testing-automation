# Automatización QA para SauceDemo

## Propósito del proyecto
Automatizar flujos básicos del sitio de pruebas [saucedemo.com](https://www.saucedemo.com) como parte de una pre-entrega del curso de Automatización QA. Las pruebas cubren el inicio de sesión, la navegación por el inventario y las operaciones simples del carrito para validar la experiencia de usuario.

## Tecnologías utilizadas
- Python 3.11+
- Selenium WebDriver
- Pytest
- webdriver-manager
- pytest-html (reporte en formato HTML)
- Google Chrome / Chromium como navegador de ejecución

## Funcionalidades Automatizadas:

* Login Automático con credenciales válidas.
* Validación de acceso a la página de inventario.
* Verificación de productos visibles y título de página.
* Agregar un producto al carrito y validar el contador.
* Navegar al carrito y comprobar el producto agregado.


## Instalación de dependencias
1. Crear y activa un entorno virtual (opcional).
2. Instala las dependencias necesarias:
   Instalar los paquetes manualmente:
   ```bash
   pip install selenium pytest webdriver-manager pytest-html
   ```

## Ejecución de pruebas
Ejecutar la suite completa y genera un reporte HTML autocontenido con el siguiente comando:
```bash
pytest -v --html=report.html --self-contained-html
```
También puedes utilizar el script auxiliar incluido:
```bash
python run_test.py
```
