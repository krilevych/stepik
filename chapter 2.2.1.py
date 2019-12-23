from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # my code
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_xpath("//input[@id='robotsRule']")
    option2.click()

    button = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    button.click()

    time.sleep(10)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()