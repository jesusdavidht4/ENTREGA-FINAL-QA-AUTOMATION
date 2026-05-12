from pages.login_pages import LoginPage
from pages.orden_page import OrdenPage
from data.ordenamiento import ORDENAMIENTO
import pytest

@pytest.mark.parametrize("valor, orden_esperado", ORDENAMIENTO)
def test_ordenar_productos(driver, valor, orden_esperado):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    orden = OrdenPage(driver)
    orden.ordenar_por(valor)

    if valor == "az":
        nombres = orden.obtener_nombres_productos()
        assert nombres == sorted(nombres)
    elif valor == "za":
        nombres = orden.obtener_nombres_productos()
        assert nombres == sorted(nombres, reverse=True)
    elif valor == "lohi":
        precios = orden.obtener_precios_productos()
        assert precios == sorted(precios)
    elif valor == "hilo":
        precios = orden.obtener_precios_productos()
        assert precios == sorted(precios, reverse=True)