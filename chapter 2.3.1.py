from this import s

from selenium import webdriver
import time
import os
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # my code

    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(y)

    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    button.click()

    time.sleep(10)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()