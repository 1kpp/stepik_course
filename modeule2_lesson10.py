from selenium import webdriver
import math


# define a function wich calculates and returnes the result in accordance with the "X"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# open the browser and get the link
wd = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
wd.get(link)

# find and click button which opens new window
button = wd.find_element_by_class_name("trollface.btn.btn-primary")
button.click()

# driver switches to new window
new_window = wd.window_handles[1]
wd.switch_to_window(new_window)

# find element which contains "X" and calculates the function
num = wd.find_element_by_id("input_value")
num_text = num.text
answer = calc(num_text)

# find field and write down answer there
answer_field = wd.find_element_by_id("answer")
answer_field.send_keys(answer)

# submit test
submit = wd.find_element_by_class_name("btn.btn-primary")
submit.click()


