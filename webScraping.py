import time
from selenium import webdriver
import re
from datetime import datetime
start = time.time()
driver = webdriver.Chrome(r'C:\Users\admin\Desktop\stock\chromedriver_win32/chromedriver')
driver.set_window_position(0, 0)
driver.set_window_size(1500, 780)
driver.get('https://kite.zerodha.com/')

user = 'WX2233'
passwd = 'amar@66464'

driver.find_element_by_id("userid").send_keys(user)
time.sleep(2)
driver.find_element_by_id("password").send_keys(passwd)
time.sleep(2)
driver.find_element_by_css_selector("button.button-orange.wide").click()
time.sleep(5)