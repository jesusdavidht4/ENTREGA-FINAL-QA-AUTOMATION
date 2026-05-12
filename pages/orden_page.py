from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class OrdenPage:
    _FILTRO = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    _NOMBRES_PRODUCTOS = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    _PRECIOS = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def ordenar_por(self, valor):
        filtro = self.wait.until(
            EC.presence_of_element_located(self._FILTRO)
        )
        Select(filtro).select_by_value(valor)

    def obtener_nombres_productos(self):
        productos = self.driver.find_elements(*self._NOMBRES_PRODUCTOS)
        return [p.text for p in productos]

    def obtener_precios_productos(self):
        precios = self.driver.find_elements(*self._PRECIOS)
        return [float(p.text.replace("$", "")) for p in precios]