import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/WebTable.html")
driver.implicitly_wait(5)

more = driver.find_element_by_link_text('More')
more.click()
loader = driver.find_element_by_css_selector('[href="DynamicData.html"]')
loader.click()
time.sleep(3)
h3 = driver.find_element_by_css_selector('.cont_box_center > h3')
h3 = h3.text
assert h3 == "Loading the data Dynamically"
driver.find_element_by_id('save').click()
time.sleep(3)
att = driver.find_element_by_css_selector('#loading>img')
att = att.get_attribute('src')
print(att)

time.sleep(3)
driver.quit()