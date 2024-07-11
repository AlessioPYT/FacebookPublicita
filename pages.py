from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import random
from driver_manager import Driver

class WaitRandomTime:
    def __init__(self, min_seconds, max_seconds):
        self.wait_time = random.randint(min_seconds, max_seconds)
        self.end_time = datetime.now() + timedelta(seconds=self.wait_time)
    
    def __call__(self, driver):
        return datetime.now() >= self.end_time


class LogPass():
    login_in_id = "email"
    password_in_id = "pass"
    button_enter_name = "login"

    def __init__(self, driver):
        self.driver = driver

    def login(self, login, password):
        self.driver.find_element(By.ID, self.login_in_id).clear()
        self.driver.find_element(By.ID, self.login_in_id).send_keys(login)
        self.driver.find_element(By.ID, self.password_in_id).clear()
        self.driver.find_element(By.ID, self.password_in_id).send_keys(password)
        self.driver.find_element(By.NAME, self.button_enter_name).click()

    def click_button(self, adress):
        self.driver.find_element(By.XPATH, adress).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adress)))

    def insert_info(self, text):
        self.driver.find_element(By.XPATH, text).send_keys()

    def is_element_present(self, by, value):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((by, value)))
            return True
        except:
            return False
