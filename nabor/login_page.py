from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def vypln_prihlasovacie_meno(self,prihlasovacie_meno):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))).send_keys(prihlasovacie_meno)

    def vypln_heslo(self, prihlasovacie_heslo):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))).send_keys(prihlasovacie_heslo)

    def klikni_na_login(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))).click()

    def login(self,prihlasovacie_meno,prihlasovacie_heslo):
        self.vypln_prihlasovacie_meno(prihlasovacie_meno)
        self.vypln_heslo(prihlasovacie_heslo)
        self.klikni_na_login()