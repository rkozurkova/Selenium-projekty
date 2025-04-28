import pytest
from selenium import webdriver
from cart_page import CartPage
from checkout_page import CheckoutPage
from inventory_page import InventoryPage
from login_page import LoginPage
from overview_page import OverviewPage
from checkout_complete_page import CheckoutCompletePage

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
    checkout_page = CheckoutPage(driver)
    overview_page = OverviewPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    login_page.login("standard_user","secret_sauce")
    inventory_page.test_potvrd_prihlasenie()
    inventory_page.vyber_ruksak()
    inventory_page.vyber_bundu()
    inventory_page.potvrd_pocet_predmetov_kosik()
    inventory_page.klikni_na_kosik()
    cart_page.klikni_na_checkout()
    checkout_page.test_formular()
    checkout_page.vypln_formular("Jan","Novák","00000")
    checkout_page.klikni_pokracovat()
    overview_page.klikni_na_finish()
    checkout_complete_page.test_uspesna_objednavka()

