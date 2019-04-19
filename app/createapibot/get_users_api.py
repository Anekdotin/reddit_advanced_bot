
import time

from selenium import webdriver
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
driver.get('http://reddit.com/')

form = driver.find_element_by_id("login_login-main")
username = form.find_element_by_name("user")
username.clear()
username.send_keys("username")

password = form.find_element_by_name("passwd")
password.clear()
password.send_keys("password")

submit = form.find_element_by_xpath("//button[. = 'login']")
submit.click()

print(driver.current_url)

# Close the browser!
# driver.quit()