import math
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# find_elements_by_link_text
# find_element By.XPATH

def get_link_text():
    value = str(math.ceil(math.pow(math.pi, math.e) * 10000))  # 224592
    return value


link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    linkA = browser.find_element_by_link_text(get_link_text())
    linkA.click()

    input1 = browser.find_element(By.XPATH, "//input[@name='first_name']")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.XPATH, "//input[@name='last_name']")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.XPATH, "//input[@name='firstname']")
    input3.send_keys("Smolensk")

    input4 = browser.find_element(By.XPATH, "//input[@id='country']")
    input4.send_keys("Russia")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
