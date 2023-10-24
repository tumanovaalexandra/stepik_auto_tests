from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # находим поле и вписываем y
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # установить чек-бокс
    option1 = browser.find_element(By.CSS_SELECTOR, ".form-check.form-check-custom .form-check-label")
    option1.click()

    # установить  radiobutton "Robots rule!"
    option2 = browser.find_element(By.CSS_SELECTOR, ".form-check.form-radio-custom .form-check-label")
    option2.click()

    # нажать Submit
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

    # time.sleep(30)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла


