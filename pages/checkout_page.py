from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class CheckoutPage:
    _BTN_ADD_TO_CART  = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    _CART_LINK        = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    _BTN_CHECKOUT     = (By.CSS_SELECTOR, "[data-test='checkout']")
    _FIRST_NAME       = (By.CSS_SELECTOR, "[data-test='firstName']")
    _LAST_NAME        = (By.CSS_SELECTOR, "[data-test='lastName']")
    _POSTAL_CODE      = (By.CSS_SELECTOR, "[data-test='postalCode']")
    _BTN_CONTINUE     = (By.CSS_SELECTOR, "[data-test='continue']")
    _BTN_FINISH       = (By.CSS_SELECTOR, "[data-test='finish']")
    _CONFIRMATION_MSG = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def agregar_primer_producto(self):
        logger.info("Agregando primer producto al carrito")
        self.wait.until(
            EC.element_to_be_clickable(self._BTN_ADD_TO_CART)
        ).click()

    def ir_al_carrito(self):
        logger.info("Navegando al carrito")
        self.driver.find_element(*self._CART_LINK).click()

    def iniciar_checkout(self):
        logger.info("Iniciando checkout")
        boton = self.wait.until(
            EC.presence_of_element_located(self._BTN_CHECKOUT)
        )
        self.driver.execute_script("arguments[0].click();", boton)

    def completar_formulario(self, first_name, last_name, postal_code):
        logger.info(f"Completando formulario: {first_name} {last_name} {postal_code}")
        self.wait.until(EC.presence_of_element_located(self._FIRST_NAME))

        def fill_react_input(selector, value):
            self.driver.execute_script("""
                var input = document.querySelector(arguments[0]);
                var nativeInputValueSetter = Object.getOwnPropertyDescriptor(
                    window.HTMLInputElement.prototype, 'value').set;
                nativeInputValueSetter.call(input, arguments[1]);
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new Event('change', { bubbles: true }));
            """, selector, value)

        fill_react_input('[data-test="firstName"]', first_name)
        fill_react_input('[data-test="lastName"]', last_name)
        fill_react_input('[data-test="postalCode"]', postal_code)

        boton = self.wait.until(EC.presence_of_element_located(self._BTN_CONTINUE))
        self.driver.execute_script("arguments[0].click();", boton)

    def finalizar_compra(self):
        logger.info("Finalizando compra")
        boton = self.wait.until(
            EC.presence_of_element_located(self._BTN_FINISH)
        )
        self.driver.execute_script("arguments[0].click();", boton)

    def obtener_mensaje_confirmacion(self):
        return self.wait.until(
            EC.presence_of_element_located(self._CONFIRMATION_MSG)
        ).text