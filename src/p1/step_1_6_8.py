# Блок 1.6. Шаг 8
# https://stepik.org/lesson/138920/step/8?unit=196194

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def find_element_xpath(browser, selector):
    """find_element By.XPATH"""
    return browser.find_element(By.XPATH, selector)


def start(link, timeout):
    browser = webdriver.Chrome()
    try:
        browser.get(link)

        find_element_xpath(browser, "//input[@name='first_name']").send_keys("Ivan")
        find_element_xpath(browser, "//input[@name='last_name']").send_keys("Petrov")
        find_element_xpath(browser, "//input[@name='firstname']").send_keys("Smolensk")
        find_element_xpath(browser, "//input[@id='country']").send_keys("Russia")

        find_element_xpath(browser, "//button[@type='submit']").click()
        print('...Button clicked')

    finally:
        time.sleep(timeout)
        browser.quit()  # закрываем браузер после всех манипуляций


if __name__ == "__main__":
    link = "http://suninjuly.github.io/find_xpath_form"
    print('Start with link: ' + link)
    start(link, 30)

# не забываем оставить пустую строку в конце файла
