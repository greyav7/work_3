import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.get("http://demo.automationtesting.in/WebTable.html")
time.sleep(8)

Switch = driver.find_element_by_link_text('SwitchTo')
Switch.click()
alert = driver.find_element_by_css_selector('[href="Alerts.html"]')
alert.click()
time.sleep(6)
driver.find_element_by_class_name('btn-danger').click()
time.sleep(8)
alert = driver.switch_to.alert
alert_text = alert.text
if alert_text == "I am an alert box!":
    print('yes')
else:
    print('no', alert_text)
alert.accept()

current_page = driver.current_url
print(current_page)

time.sleep(6)

# driver.execute_script("window.open();")
# window_after = driver.window_handles[1]
# driver.switch_to.window(window_after)
# driver.get(current_page)

alert_and_cancel = driver.find_element_by_css_selector('[href="#CancelTab"]')
alert_and_cancel.click()
driver.find_element_by_class_name('btn-primary').click()
time.sleep(3)
confirm = driver.switch_to.alert
confirm.dismiss()

time.sleep(6)
driver.execute_script("window.open();")
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.get(current_page)
time.sleep(3)
alert_text = driver.find_element_by_css_selector('[href="#Textbox"]')
alert_text.click()
driver.find_element_by_class_name('btn-info').click()
time.sleep(3)
prompt = driver.switch_to.alert
prompt.send_keys("Ура!")
prompt.accept()

time.sleep(6)
driver.quit()
