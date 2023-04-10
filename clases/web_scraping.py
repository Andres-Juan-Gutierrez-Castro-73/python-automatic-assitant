from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductSearcher:
    def __init__(self, sites):
        self.sites = sites
        self.service = Service('../static/chromedriver.exe')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--start-maximized')
        self.drivers = [webdriver.Chrome(service=self.service, options=self.options) for _ in range(len(sites))]
        
    def search_products(self, query):
        for i, site in enumerate(self.sites):
            self.drivers[i].get(site)
            search_box = WebDriverWait(self.drivers[i], 10).until(EC.presence_of_element_located((By.NAME, 'as_word')))
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
            products = WebDriverWait(self.drivers[i], 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.ui-search-item__title')))
            for product in products:
                print(product.text)
                
    def close_browsers(self):
        for driver in self.drivers:
            driver.quit()