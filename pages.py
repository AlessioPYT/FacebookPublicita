from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from driver_manager import Driver
from conftest import driver
import random
import allure
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='test_log.log')


class LogPass:
    login_in_id = "email"
    password_in_id = "pass"
    button_enter_name = "login"

    def __init__(self, driver):
        self.driver = driver

    def login(self, login, password):
        with allure.step("If login need"):
            logging.info("login is normal")
            self.driver.find_element(By.ID, self.login_in_id).clear()
            self.driver.find_element(By.ID, self.login_in_id).send_keys(login)
            self.driver.find_element(By.ID, self.password_in_id).clear()
            self.driver.find_element(By.ID, self.password_in_id).send_keys(password)
            self.driver.find_element(By.NAME, self.button_enter_name).click()

    def click_button(self, xpath):
        with allure.step("Click button"):
            try:
                logging.info("Attempting to click button")
                button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                button.click()
                logging.info("Button clicked successfully")
            except Exception as e:
                logging.error(f"Failed to click button: {e}")
                raise

    def insert_info(self, xpath, text):
        with allure.step("Insert text"):
            logging.info("insert info started")
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element.clear()
            element.send_keys(text)
            logging.info("insert info seccussful")

    def open_link(self, url):
        with allure.step("is url open"):
            logging.info("open link stareted")
            self.driver.get(url)
            logging.info("open link succesful")

    def file_element(self, xpath, file_path):
        with allure.step("Upload file"):
            logging.info("file element was started")
            element = self.driver.find_element(By.XPATH, xpath)
            element.send_keys(file_path)
            logging.info("file element was succesful")

    def is_element_present(self, by, value):
        try:
            logging.info(f"Checking presence of element by {by} with value {value}")
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, value)))
            return True
        except Exception as e:
            logging.error(f"Element not found: {e}")
            return False