from selenium.webdriver.chrome.webdriver import WebDriver
from pages import LogPass
import pytest
import random
from selenium.webdriver.common.by import By
from XPATH_info import *
import logging
import time
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='test_log.log')


def random_wait(min_seconds, max_seconds):
    wait_time = random.randint(min_seconds, max_seconds)
    logging.info(f"Waiting for {wait_time} seconds")
    time.sleep(wait_time)


def random_info(some_dict: dict):
    return some_dict.get(random.randint(1, len(some_dict)))


def test_publicita(driver): 
    logging.info("Starting test_publicita")
    logpass = LogPass(driver)
    if logpass.is_element_present(By.ID, "email"):
        logpass.login(login, password)
    while True:  
        logpass.open_link(random_info(some_groups))  
        logpass.click_button(insert_text) 
        logpass.insert_info(publication_create, random_info(some_text))  
        logpass.click_button(foto_video_button)
        logpass.file_element(add_foto, foto_publicita)
        random_wait(180, 520)  



if __name__ == "__main__":
    pytest.main()  

