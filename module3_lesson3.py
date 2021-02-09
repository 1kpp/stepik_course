from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
#open the browser
driver.get("http://suninjuly.github.io/selects1.html")

#look for two numbers, find their sum and parse to string
num1_el = driver.find_element_by_id("num1")
num1 = num1_el.text
num2_el = driver.find_element_by_id("num2")
num2 = num2_el.text
result = int(num1) + int(num2)
final_result = str(result)

#look for the element in a dropdown list equal to the sum of two numbers
select = Select(driver.find_element_by_id("dropdown"))
select.select_by_value(final_result)
submit = driver.find_element_by_css_selector("[class='btn btn-default']")
submit.click()

time.sleep(90)
driver.quit()
