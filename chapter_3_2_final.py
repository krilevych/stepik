from selenium import webdriver
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//input[@placeholder='Input your name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        input2.send_keys("Lviv")
        button = browser.find_element_by_xpath("//button[contains(text(),'Submit')]")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_abs2(self):
         link = "http://suninjuly.github.io/registration1.html"
         browser = webdriver.Chrome()
         browser.get(link)

         input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
         input1.send_keys("Ivan")
         input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
         input2.send_keys("Petrov")
         input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
         input3.send_keys("Lviv")
         button = browser.find_element_by_xpath("//button[contains(text(),'Submit')]")
         button.click()

         welcome_text_elt = browser.find_element_by_tag_name("h1")
         welcome_text = welcome_text_elt.text

         assert "Congratulations! You have successfully registered!" == welcome_text
         self.assertEqual("Congratulations! You have succвessfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()

