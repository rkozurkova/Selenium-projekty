from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutCompletePage:

    def __init__(self, driver):
        self.driver = driver

    def test_uspesna_objednavka(self):
        uspesna_objednavka = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='THANK YOU FOR YOUR ORDER']")))
        assert "THANK YOU FOR YOUR ORDER" in uspesna_objednavka.text, f"Nadpis na stránke ukončenia objednávky sa nezobrazil"
        assert "checkout-complete.html" in self.driver.current_url, f"Stránka ukončenia objednávky sa nezobrazila, aktuálne url: {self.driver.current_url}"