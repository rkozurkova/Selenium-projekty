from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RecruitmentPage:
    def __init__(self,driver):
        self.driver = driver

    def vyber_pracovnu_poziciu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'oxd-select-text-input') and text()='-- Select --']")))
        pracovna_pozicia = self.driver.find_element(By.XPATH,
                                               "//div[contains(@class, 'oxd-select-text-input') and text()='-- Select --']")
        pracovna_pozicia.click()
        vyber = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='option']/span[text()='QA Lead']")))
        vyber.click()

    def vyber_volne_miesto(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//label[text()='Vacancy']/following::div[@class='oxd-select-text-input'][1]")))
        self.driver.find_element(By.XPATH,
                            "//label[text()='Vacancy']/following::div[@class='oxd-select-text-input'][1]").click()
        self.driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Senior QA Lead']").click()

    def vyber_status(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//label[text()='Status']/following::div[@class='oxd-select-text-input'][1]")))
        self.driver.find_element(By.XPATH,
                            "//label[text()='Status']/following::div[@class='oxd-select-text-input'][1]").click()
        self.driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Shortlisted']").click()

    def potvrd_vyber(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']"))).click()


