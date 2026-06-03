import pytest
from faker import Faker
from pages.login_pages import LoginPage
from pages.checkout_page import CheckoutPage
from utils.helpers import load_user_csv
import logging

logger = logging.getLogger(__name__)
fake = Faker()

CHECKOUT_DATA = load_user_csv("data/checkout.csv")

@pytest.mark.parametrize("first_name, last_name, postal_code", CHECKOUT_DATA)
def test_checkout_completo(driver, first_name, last_name, postal_code):
    logger.info(f"Iniciando test checkout: {first_name} {last_name}")

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    checkout = CheckoutPage(driver)
    checkout.agregar_primer_producto()
    checkout.ir_al_carrito()
    checkout.iniciar_checkout()
    checkout.completar_formulario(first_name, last_name, postal_code)
    checkout.finalizar_compra()

    mensaje = checkout.obtener_mensaje_confirmacion()
    assert mensaje == "Thank you for your order!"

@pytest.mark.parametrize("_", [None])
def test_checkout_con_faker(_,driver):
    first_name  = fake.first_name()
    last_name   = fake.last_name()
    postal_code = fake.postcode()
    logger.info(f"Checkout con Faker: {first_name} {last_name} {postal_code}")

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    checkout = CheckoutPage(driver)
    checkout.agregar_primer_producto()
    checkout.ir_al_carrito()
    checkout.iniciar_checkout()
    checkout.completar_formulario(first_name, last_name, postal_code)
    checkout.finalizar_compra()

    mensaje = checkout.obtener_mensaje_confirmacion()
    assert mensaje == "Thank you for your order!"