from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PrecioPage:
    _PRECIOS = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_precio_producto(self, indice):
        precios = self.wait.until(
            EC.presence_of_all_elements_located(self._PRECIOS)
        )
        return precios[indice].text