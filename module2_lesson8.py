from selenium import webdriver
import os

#open the link
link = 'http://suninjuly.github.io/file_input.html'
driver = webdriver.Chrome()
driver.get(link)

#fill each field
fname = driver.find_element_by_css_selector("[placeholder='Enter first name']")
fname.send_keys("Vasya")
lname = driver.find_element_by_css_selector("[placeholder='Enter last name']")
lname.send_keys("Vasiliev")
email = driver.find_element_by_css_selector("[placeholder='Enter email']")
email.send_keys("email@email")

#upload a file
file_button = driver.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
file_button.send_keys(file_path)

#click submit
submit = driver.find_element_by_css_selector("[type='submit']")
submit.click()