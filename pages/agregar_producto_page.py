from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AgregarProductoPage:
    _NOMBRES_PRODUCTOS = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    _BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    _NOMBRE_EN_CARRITO = (By.CSS_SELECTOR, ".cart_item [data-test='inventory-item-name']")  # ✅ específico del carrito

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_nombre_producto(self, indice):
        productos = self.driver.find_elements(*self._NOMBRES_PRODUCTOS)
        return productos[indice].text

    def agregar_producto(self, indice):
        botones = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//button[contains(text(),'Add to cart')]")
            )
        )
        botones[indice].click()

    def obtener_badge(self):
        return self.driver.find_element(*self._BADGE).text

    def ir_al_carrito(self):
        self.driver.find_element(*self._CART_LINK).click()

    def obtener_nombre_en_carrito(self):
        return self.wait.until(
            EC.presence_of_element_located(self._NOMBRE_EN_CARRITO)  # ✅
        ).text