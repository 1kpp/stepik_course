from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

#define a function wich calculates and returnes the result in accordance with the "X"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
#open the browser
link = "http://SunInJuly.github.io/execute_script.html"
driver.get(link)

#find element which contains "X" and calculates the function
x_element = driver.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
#enter the result of calculations into the text area
driver.find_element_by_id("answer").send_keys(y)
#scroll down the page to make another elements visible
submit = driver.find_element_by_css_selector("[class='btn btn-primary']")
driver.execute_script("return arguments[0].scrollIntoView(true);", submit)
submit.click()
#check radiobutton and checkbox
option1 = driver.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()
option2 = driver.find_element_by_css_selector("[for='robotsRule']")
option2.click()
#click submit
submit.click()

