from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self,driver):
        self.driver = driver

    def odstran_ruksak(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//button[@class='btn_secondary cart_button'][normalize-space()='REMOVE'])[1]"))).click()

    def odstran_bundu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='REMOVE']"))).click()

    def pokracuj_v_nakupe(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[normalize-space()='Continue Shopping']"))).click()
