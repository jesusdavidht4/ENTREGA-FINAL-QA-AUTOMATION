from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    _PRODUCTOS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    _NOMBRE_PRODUCTO = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_productos(self):
        return self.driver.find_elements(*self._PRODUCTOS)
    
    def obtener_nombre_producto(self, indice):
        productos = self.obtener_productos()
        return productos[indice].find_element(*self._NOMBRE_PRODUCTO).text
    
