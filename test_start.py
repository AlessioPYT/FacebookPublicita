from pages import LogPass
from pages import WaitRandomTime
import pytest
import random
from selenium.webdriver.common.by import By
from XPATH_info import *
import logging
from driver_manager import Driver
from conftest import driver

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='test_log.log')

# def random_info(some_dict: dict):
#     return some_dict.get(random.randint(1, len(some_dict)))

def random_info(some_dict: dict):
    return random.choice(list(some_dict.values()))


def test_publicita(driver): 
    logging.info("Starting test_publicita")
    wait = WaitRandomTime(180, 520)
    logpass = LogPass(driver)
    if logpass.is_element_present(By.ID, "email"):
        logpass.login(login, password)
    while True:  
        logpass.open_link(random_info(some_groups))  
        logpass.click_button(insert_text) 
        logpass.insert_info(publication_create, random_info(some_text))  
        logpass.click_button(foto_video_button)
        logpass.file_element(add_foto, foto_publicita)
        
        wait(180, 520)  



if __name__ == "__main__":
    pytest.main()  

