from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text

    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text

    z = int(x)+int(y)



    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))


    # нажать Submit
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла
