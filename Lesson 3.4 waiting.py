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
time.sleep(3)
more = driver.find_element_by_link_text('More')
more.click()
loader = driver.find_element_by_css_selector('[href="Loader.html"]')
loader.click()
time.sleep(5)

run_btn = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.ID, "loader"),"Run"))
driver.find_element(By.ID, "loader").click()
Lorem = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".modal-body > p"),"Lorem"))
Save = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer .btn-primary")))
time.sleep(3)
driver.quit()