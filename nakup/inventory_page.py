from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self,driver):
        self.driver = driver

    def test_potvrd_prihlasenie(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='product_label']")))
        produkty_nadpis = self.driver.find_element(By.XPATH,"//div[@class='product_label']")
        assert "Products" in produkty_nadpis.text, f"Prihlásenie zlyhalo, text 'Products' sa na stránke nenachádza"

    def vyber_ruksak(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='inventory_list']//div[1]//div[3]//button[1]"))).click()

    def vyber_bundu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Fleece Jacket']]//button"))).click()

    def potvrd_pocet_predmetov_kosik(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='fa-layers-counter shopping_cart_badge']")))
        kosik = self.driver.find_element(By.XPATH, "//span[@class='fa-layers-counter shopping_cart_badge']")
        assert kosik.text == "2", f"Očakávaný počet predmetov v košíku :2, aktuálny počet : {kosik.text} "

    def klikni_na_kosik(self):
       WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link fa-layers fa-fw']//*[name()='svg']"))).click()

