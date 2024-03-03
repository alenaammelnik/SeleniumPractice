from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'
browser  = webdriver.Chrome()
browser.get(link)

try:
    trollface = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary')
    trollface.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element  = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    time.sleep(10)
    browser.quit()




