from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginErrorPage:
    _ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_mensaje_error(self):
        return self.wait.until(
            EC.presence_of_element_located(self._ERROR_MSG)
        ).text