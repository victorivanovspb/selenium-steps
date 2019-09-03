# find_elements_by_xpath

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_xpath("//input[@type='text']")
    for element in elements:
        element.send_keys("Text")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()  # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
