from selenium import webdriver
from selenium.webdriver.common.by import By

# find_element By.XPATH

import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # input1 = browser.find_element_by_tag_name("input")
    input1 = browser.find_element(By.XPATH, "//input[@name='first_name']")
    input1.send_keys("Ivan")

    #input2 = browser.find_element_by_name(value2)
    input2 = browser.find_element(By.XPATH, "//input[@name='last_name']")
    input2.send_keys("Petrov")

    #input3 = browser.find_element_by_class_name(value3)
    input3 = browser.find_element(By.XPATH, "//input[@name='firstname']")
    input3.send_keys("Smolensk")

    #input4 = browser.find_element_by_id(value4)
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
