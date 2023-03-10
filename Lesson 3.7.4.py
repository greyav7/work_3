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
loader = driver.find_element_by_css_selector('[href="JqueryProgressBar.html"]')
loader.click()
time.sleep(3)

button = WebDriverWait(driver, 5).until(
    EC. invisibility_of_element_located((By.CLASS_NAME, "ui-dialog-buttonset")))

driver.find_element(By.ID, "downloadButton").click()
cancel = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "ui-dialog-buttonset"),"Cancel Download"))

close = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "ui-dialog-buttonset"),"Close"))
driver.find_element(By.CLASS_NAME, "ui-dialog-buttonset").click()
driver.find_element(By.ID, "downloadButton").click()

complete = WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element((By.ID, "dialog"),"Complete!"))

time.sleep(3)
driver.quit()