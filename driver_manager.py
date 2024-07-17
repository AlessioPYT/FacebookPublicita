from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='test_log.log')

class Driver():
    driver = None

    @classmethod
    def start(cls):
        logging.info("Start Browser")
        options = Options()
        options.add_argument("dom.webnotifications.enabled")
        prefs = {"profile.default_content_setting_values.notifications": 2}  # Отключить уведомления
        options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument("--headless")   # фоновий режим
        options.add_argument("user-data-dir=C:\\Users\\Алексей\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1") # свой профиль          
        cls.driver = webdriver.Chrome(options=options)
        return cls.driver
    
    @classmethod
    def open_browser(cls):
        logging.info("Opening browser from driver")
        cls.driver.get("https://www.facebook.com/")
        # WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))                        
        return cls.driver    
        
    @classmethod                                        
    def finish(cls):
        if cls.driver:
            logging.info("Close driver")
            cls.driver.quit()


        
