import pytest
from selenium import webdriver
from login_page import LoginPage
from cart_page import CartPage
from inventory_page import InventoryPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_nakup(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.login("standard_user","secret_sauce")
    inventory_page.test_potvrd_prihlasenie()
    inventory_page.vyber_ruksak()
    inventory_page.vyber_bundu()
    inventory_page.klikni_na_kosik()
    inventory_page.test_potvrd_pocet_predmetov_kosik()
    cart_page.odstran_ruksak()
    cart_page.odstran_bundu()
    cart_page.test_prazdny_kosik()
    cart_page.pokracuj_v_nakupe()