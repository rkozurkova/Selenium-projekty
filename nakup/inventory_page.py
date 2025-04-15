from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self,driver):
        self.driver = driver

    def vyber_ruksak(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='inventory_list']//div[1]//div[3]//button[1]"))).click()

    def vyber_bundu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Fleece Jacket']]//button"))).click()

    def klikni_na_kosik(self):
       WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link fa-layers fa-fw']//*[name()='svg']"))).click()

