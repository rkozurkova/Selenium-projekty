from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self,driver):
        self.driver = driver

    def klikni_na_recruitment(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Recruitment']"))).click()

