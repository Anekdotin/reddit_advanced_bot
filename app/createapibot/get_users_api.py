from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
import time

options.headless = True
driver = webdriver.Firefox(options=options, executable_path="/home/bot/reddit/venv/lib/python3.5/geckodriver")
driver.set_window_size(1120, 550)
driver.get('https://www.reddit.com/login?dest=https%3A%2F%2Fwww.reddit.com%2F')

# get the form
form = driver.find_element_by_class_name("AnimatedForm")

#login to form
username = form.find_element_by_id("loginUsername")
username.clear()
username.send_keys("Mirbekov46")

password = form.find_element_by_id("loginPassword")
password.clear()
password.send_keys("BE4M1HJ63T01VBK8IJKRILMDX2")

submit = form.find_element_by_class_name("AnimatedForm__submitButton")
submit.click()
time.sleep(2)



# go back to reddit
driver.get('https://www.reddit.com/prefs/apps')

print(driver.current_url)
time.sleep(4)

driver.save_screenshot("1231.png")

form_button = driver.find_element_by_class_name("edit-app-form")
form_button.click()

time.sleep(2)

driver.save_screenshot("12312.png")



#fill out the form
y = driver.find_element_by_name("name").is_enabled()
print(y)
if y is True:
    gettable = driver.find_element_by_class_name("preftable")

    nameinput = gettable.find_element_by_name("name")
    nameinput.send_keys("firstapp")
    descripinput = gettable.find_element_by_name("description")
    descripinput.send_keys("for science")
else:
    print("not enabled")
driver.quit()


