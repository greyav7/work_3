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
loader = driver.find_element_by_css_selector('[href="FileUpload.html"]')
loader.click()
time.sleep(3)
file = (r'C:\Users\kunae_000\Desktop\Фото на заставки\IMG_9663.jpg')
f = driver.find_element_by_id('input-4')
f.send_keys(file)

remove = driver.find_element_by_css_selector('.glyphicon.glyphicon-trash')
remove.click()
ivan = (r'C:\Users\kunae_000\Desktop\Ivan.txt')
i = driver.find_element_by_id('input-4')
i.send_keys(ivan)

update = driver.find_element_by_css_selector('.fileinput-upload.fileinput-upload-button')
update = update.get_attribute('disabled')
if update is not None:
    print ('blocked')
else:
    print('no blocked')
driver.find_element_by_css_selector('.kv-error-close')
time.sleep(3)
driver.quit()