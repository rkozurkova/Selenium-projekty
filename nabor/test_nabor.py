from selenium import webdriver
import pytest
from login_page import LoginPage
from dashboard_page import DashboardPage
from recruitment_page import RecruitmentPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_nabor(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    recruitment_page = RecruitmentPage(driver)

    login_page.login("Admin","admin123")
    dashboard_page.klikni_na_recruitment()
    recruitment_page.vyber_pracovnu_poziciu()
    recruitment_page.vyber_status()
    recruitment_page.vyber_volne_miesto()
    recruitment_page.potvrd_vyber()

    vypis_spravy = recruitment_page.najdi_pocet_vyskytov()
    assert vypis_spravy.startswith("(") and vypis_spravy.endswith("Records Found"), f"Neočakávaný formát: {vypis_spravy}"
    vypis_cisla = vypis_spravy[1:vypis_spravy.index(")")]
    assert vypis_cisla.isdigit(), f"Očakávané číslo v (), namiesto toho: {vypis_cisla} "
