from this import s

from selenium import webdriver
import time
import math
from math import log, sin

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # my code

    def calc(x):
        return str(log(abs(12*sin(int(x)))))

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")
    time.sleep(6)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_xpath("//input[@id='robotsRule']")
    option2.click()



    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


    time.sleep(10)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()