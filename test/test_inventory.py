from pages.login_pages import LoginPage
from pages.Inventory_page import InventoryPage
from data.productos import PRODUCTOS
import pytest

@pytest.mark.parametrize("indice, nombre_esperado", PRODUCTOS)
def test_catalogo_productos(driver, indice, nombre_esperado):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    productos = inventory.obtener_productos()
    assert len(productos) > 0

    nombre = inventory.obtener_nombre_producto(indice)
    assert nombre == nombre_esperado