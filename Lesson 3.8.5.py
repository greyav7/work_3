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
Switch = driver.find_element_by_link_text('SwitchTo')
Switch.click()
win = driver.find_element_by_css_selector('[href="Windows.html"]')
win.click()
time.sleep(2)

new_win = driver.find_element_by_css_selector('[href="http://www.selenium.dev"]')
new_win.click()

window_1 = driver.window_handles[1]
driver.switch_to.window(window_1)
time.sleep(5)
driver.close()

window_0 = driver.window_handles[0]
driver.switch_to.window(window_0)

separ = driver.find_element_by_css_selector('[href="#Multiple"]')
separ.click()
s_win = driver.find_element_by_css_selector('[onclick="multiwindow()"]')
s_win.click()
window_2 = driver.window_handles[2]
driver.switch_to.window(window_2)

w_2 = WebDriverWait(driver, 10).until(
    EC.url_to_be('https://demo.automationtesting.in/Index.html'))
number_of_tabs = WebDriverWait(driver, 10).until(
    EC.number_of_windows_to_be(3))
print(number_of_tabs)

mail = driver.find_element_by_id('email')
mail.send_keys("565@email.com")
enter = driver.find_element_by_id('enterimg')
enter.click()
ura = WebDriverWait(driver, 10).until(
    EC.url_to_be('https://demo.automationtesting.in/Register.html'))
print("Krasavello!")
time.sleep(3)
driver.quit()


#C:/Users/kunae_000/PycharmProjects/pythonProject/Lesson3