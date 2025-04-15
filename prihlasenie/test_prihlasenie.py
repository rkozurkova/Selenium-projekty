from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def otvor_prehliadac(driver,url):
    driver.get(url)

def prihlasenie(driver,prihlasovacie_meno,prihlasovacie_heslo):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(prihlasovacie_meno)

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(prihlasovacie_heslo)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[type='submit']")))
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

def over_prihlasenie(driver):
   uspesne_prihlasenie = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//h6[normalize-space()='Dashboard']")))
   assert uspesne_prihlasenie.text == "Dashboard"

@pytest.mark.parametrize("prihlasovacie_meno, prihlasovacie_heslo, ocakavany_vysledok", [
    ("Admin","admin123", True),
    ("Admin", "nespravneheslo", False),
    ("Uzivatel", "admin123", False),
    ("","",False)
])

def test_prihlasenie(driver, prihlasovacie_meno, prihlasovacie_heslo, ocakavany_vysledok):
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    otvor_prehliadac(driver,url)
    prihlasenie(driver, prihlasovacie_meno, prihlasovacie_heslo)

    if ocakavany_vysledok:
        over_prihlasenie(driver)
    else:
        chybova_hlaska = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")))
        assert "Neplatné údaje" in chybova_hlaska.text
