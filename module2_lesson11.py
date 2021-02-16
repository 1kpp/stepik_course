from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


# define a function wich calculates and returnes the result in accordance with the "X"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# open the browser and get the link
wd = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
wd.get(link)

# finds an elements which contains price we need and waits until price = 100, then clicks "book" button
price = WebDriverWait(wd, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
button = wd.find_element_by_id("book")
button.click()

# find element which contains "X" and calculates the function
num = wd.find_element_by_id("input_value")
num_text = num.text
answer = calc(num_text)

# find field and write down answer there
answer_field = wd.find_element_by_id("answer")
answer_field.send_keys(answer)

# submit test
submit = wd.find_element_by_id("solve")
submit.click()
