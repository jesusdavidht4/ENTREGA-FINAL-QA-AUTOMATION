import pytest
from pages.login_pages import LoginPage
from utils.helpers import load_user_json, load_user_csv

# Usamos JSON para usuarios válidos
USERS = load_user_json("data/users.json")

@pytest.mark.parametrize("username, password", USERS)
def test_login_valido(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    assert "inventory" in driver.current_url