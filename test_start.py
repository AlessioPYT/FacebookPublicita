from pages import LogPass
from pages import WaitRandomTime
import pytest
import random
from selenium.webdriver.common.by import By
from XPATH_info import *


def random_info(some_dict: dict):
    return some_dict.get(random.randint(1, len(some_dict)))

def test_publicita(driver): 
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

