from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
time.sleep(20)


user_name = input()
msg = input()
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(user_name))
user.click()
msg_box = driver.find_element_by_class_name('_13mgZ')
for i in range(1000):
    msg_box.send_keys(msg)
    msg_box.send_keys(Keys.RETURN)

