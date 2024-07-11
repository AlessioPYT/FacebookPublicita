from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

login_in_id = "email"
password_in_id = "pass"
button_enter_name = "login"

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
but_groups = driver
but_groups.find_element(By.ID, login_in_id).clear()
but_groups.find_element(By.ID, login_in_id).send_keys("380631953810")
but_groups.find_element(By.ID, password_in_id).clear()
but_groups.find_element(By.ID, password_in_id).send_keys("Anetto563")
but_groups.find_element(By.NAME, button_enter_name).click()
but_groups.find_element(By.ID, password_in_id).clear()
but_groups.find_element(By.ID, password_in_id).send_keys("Anetto563")
but_groups.find_element(By.NAME, button_enter_name).click()
sleep(10)
driver.get("https://www.facebook.com/groups/1781014825372492/")
but_groups.find_element(By.XPATH, '//div[@class="x1i10hfl x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou"]').click()
sleep(10)
but_groups.find_element(By.XPATH, '//div[@aria-label="Создайте общедоступную публикацию…"]').send_keys("Hello")
sleep(10)
but_groups.find_element(By.XPATH, '//div[@aria-label="Отправить"]').click()
sleep(10)

