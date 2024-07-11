from pages import LogPass
from pages import WaitRandomTime
import pytest
from driver_manager import Driver
import random
from selenium.webdriver.common.by import By

from time import sleep


insert_text = """//*[@id="mount_0_0_6M"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span"""
groups = "//a[text()='Группы']"
enter_text = """//*[@id="mount_0_0_6M"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div/div/div/div[1]/div/span/span"""
some_dict = {
    1: """//*[@id="mount_0_0_6M"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[6]/div[1]/div/div/a/div/div/div[2]/div/div/div/div[1]/span/span""", 
    2: """//*[@id="mount_0_0_6M"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div[9]/div[1]/div/div/a/div/div/div[2]/div/div/div/div[1]/span/span/span""", 
    3: """//*[@id="mount_0_0_6M"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div[6]/div[1]/div/div/a/div/div/div[2]/div/div/div/div[1]/span/span/span"""
}

some_dict1 = {1: "hello", 2: "whats Up", 3: "Hey Guys"}

def random_info(some_dict: dict):
    return some_dict.get(random.randint(1, len(some_dict)))

def test_publicita(driver): 
    wait = WaitRandomTime(180, 520)
    logpass = LogPass(driver)
    if logpass.is_element_present(By.ID, "email"):
        logpass.login("123", "123")
    logpass.click_button(groups) # enter in groups
    while True: # start process of publicicta
        logpass.click_button(random_info(some_dict))  # random open one group
        logpass.click_button(insert_text) # click to insert text
        logpass.insert_info(random_info(some_dict1))  # insert random text from file
        logpass.click_button(enter_text)  # enter text
        # logpass.click_button( groups)  # return to the list of groups
        wait(180, 520)  # random wait from 3 minutes to 7 minutes



if __name__ == "__main__":
    pytest.main()  

