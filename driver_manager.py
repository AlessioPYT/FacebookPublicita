from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class Driver():
    driver = None

    @classmethod
    def start(cls):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")   
        chrome_options.add_argument("user-data-dir=C:\\Users\\Алексей\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")          
        cls.driver = webdriver.Chrome(options=chrome_options)
        return cls.driver
    
    @classmethod
    def open_browser(cls):
        cls.driver.get("https://ua.scryde.net/panel/?character=273205599&server=x100&action=activate")
        WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))                        
        return cls.driver    
        
    @classmethod                                        
    def finish(cls):
        if cls.driver:
            cls.driver.quit()


        