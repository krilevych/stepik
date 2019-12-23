from this import s

from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # my code

    def calc():
        return str(int(x) + int(y))

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text

    print(calc)

    option1 = browser.find_element_by_id("dropdown")
    option1.click()

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(calc()) # ищем элемент с текстом "Python"


    button = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    button.click()

    time.sleep(10)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()