from pages.login_pages import LoginPage
from pages.login_error_page import LoginErrorPage
from data.usuarios_invalidos import USUARIOS_INVALIDOS
import pytest

@pytest.mark.parametrize("username, password, mensaje_esperado", USUARIOS_INVALIDOS)
def test_login_negativo(driver, username, password, mensaje_esperado):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    error_page = LoginErrorPage(driver)
    mensaje = error_page.obtener_mensaje_error()
    assert mensaje == mensaje_esperado