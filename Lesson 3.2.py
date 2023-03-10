import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
time.sleep(4)
first_name = driver.find_element_by_css_selector('[ng-model="FirstName"]')
first_name.click()
first_name.send_keys("John")
last_name = driver.find_element_by_css_selector('[ng-model="LastName"]')
last_name.click()
last_name.send_keys("Shwarz")
email = driver.find_element_by_css_selector('[ng-model="EmailAdress"]')
email.click()
email.send_keys("Shwarz.John@abc.com")
phone = driver.find_element_by_css_selector('[ng-model="Phone"]')
phone.click()
phone.send_keys("5656556566")
gender = driver.find_element_by_css_selector('[value="Male"]')
gender.click()
country = driver.find_element_by_id('country')
Select_country = Select(country)
Select_country.select_by_value('Japan')
year = driver.find_element_by_id('yearbox')
Select_year = Select(year)
Select_year.select_by_value('1945')
month = driver.find_element_by_css_selector('[placeholder="Month"]')
Select_month = Select(month)
Select_month.select_by_value('May')
day = driver.find_element_by_id('daybox')
Select_day = Select(day)
Select_day.select_by_value('9')
password = driver.find_element_by_id("firstpassword")
password.click()
password.send_keys("5ShwarzJ")
s_password = driver.find_element_by_id("secondpassword")
s_password.click()
s_password.send_keys("5ShwarzJ")
#photo = driver.find_element_by_id("imagesrc")
#photo.click()
file = (r'C:\Users\kunae_000\Desktop\Фото на заставки\IMG_9663.jpg')
upload = driver.find_element_by_id("imagesrc") # находим селектор кнопки загрузить файл
upload.send_keys(file)
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_id("submitbtn").click() # подтверждение
time.sleep(4)
current_page = driver.current_url
page = 'http://demo.automationtesting.in/WebTable.html'
if current_page == page:
    print('Совпадает')
else:
    print('находимся на странице: '+ current_page, 'должны находиться на странице: '+ page)
time.sleep(3)
driver.get("http://demo.automationtesting.in/WebTable.html")
current_page = driver.current_url
if current_page == page:
    print('Совпадает')
else:
    print('находимся на странице: '+ current_page, 'должны находиться на странице: '+ page)
time.sleep(1)
driver.execute_script("alert('Теперь вы на той странице');")

#driver.execute_script("alert('Скрипт выполнен успешно!');")
time.sleep(3)
driver.quit()