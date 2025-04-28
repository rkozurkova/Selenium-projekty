from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def test_formular(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "first-name")))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "last-name")))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "postal-code")))

        assert self.driver.find_element(By.ID, "first-name")
        assert self.driver.find_element(By.ID, "last-name")
        assert self.driver.find_element(By.ID, "postal-code")

    def vypln_meno(self, meno):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@id='first-name']"))).send_keys(meno)

    def vypln_priezvisko(self,priezvisko):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@id='last-name']"))).send_keys(priezvisko)

    def vypln_psc(self, psc):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@id='postal-code']"))).send_keys(psc)

    def vypln_formular(self, meno, priezvisko, psc):
        self.vypln_meno(meno)
        self.vypln_priezvisko(priezvisko)
        self.vypln_psc(psc)

    def klikni_pokracovat(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@value='CONTINUE']"))).click()
