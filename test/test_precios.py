from pages.login_pages import LoginPage
from pages.precios_page import PrecioPage
from data.precios import PRECIOS
import pytest

@pytest.mark.parametrize("indice, precio_esperado", PRECIOS)
def test_precio_producto(driver, indice, precio_esperado):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    precio_page = PrecioPage(driver)
    precio = precio_page.obtener_precio_producto(indice)
    assert precio == precio_esperado