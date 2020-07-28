from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)/chromedriver.exe"   #Path of Chromedriver (Your Path may be different)
bot = webdriver.Chrome(PATH)

Name = "CodeinVeins"  #Enter Name of the person whom you want to send message

bot.get('https://web.whatsapp.com/')

time.sleep(10)  #wait for 10 secs

person = bot.find_element_by_xpath("//span[@title = '{}']".format(Name))

person.click()

msg_box = bot.find_element_by_class_name('_3uMse')


# add for loop

for i in range(1000):
    msg_box.send_keys("This message is sent using Python ")  # Type your own message
    time.sleep(1.5)
    msg_box.send_keys(Keys.RETURN)
    time.sleep(1)


