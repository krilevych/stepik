from this import s

from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # my code

    input1 = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
    input1.send_keys("Volodymyr")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Enter last name']")
    input2.send_keys("Krilevych")
    input3 = browser.find_element_by_xpath("//input[@placeholder='Enter email']")
    input3.send_keys("vova@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.png')  # добавляем к этому пути имя файла
    button = browser.find_element_by_id("file").send_keys(file_path)

    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    button.click()


    time.sleep(10)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()