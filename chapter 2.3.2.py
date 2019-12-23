from this import s

from selenium import webdriver
import time
import os
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    # my code
    button = browser.find_element_by_xpath("//button[@class='trollface btn btn-primary']")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(y)

    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    button.click()



finally:
    # закрываем браузер после всех манипуляций
    browser.quit()