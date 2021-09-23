import time
from selenium.webdriver.support.ui import WebDriverWait as WBWait
from selenium.webdriver.chrome.webdriver import WebDriver
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = WebDriver()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def reg(link, firstname, lastname, emails):
    browser.get(link)
    first = browser.find_element_by_class_name('form-control.first')
    first.send_keys(firstname)
    second = browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.second_class > input')
    second.send_keys(lastname)
    third = browser.find_element_by_class_name('form-control.third')
    third.send_keys(emails)
    button = browser.find_element_by_class_name('btn.btn-default').click()
    if EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), 'Congratulations! You have successfully registered!'):
        return True
    else:
        return False


# try:
#     link = "http://suninjuly.github.io/explicit_wait2.html"
#     browser.get(link)
#     book = browser.find_element_by_id("book")
#     books = WBWait(browser, 15)\
#         .until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
#     book.click()
#     # window = browser.window_handles[1]
#     # browser.switch_to.window(window)
#     # fills = "No matter what I type"
#     # diro = "C:/Users/evgeniy.popov/Desktop/text.txt"
#     firstName = browser.find_element_by_id('input_value').text
#     lastName = calc(firstName)
#     email = browser.find_element_by_id('answer').send_keys(lastName)
#     button2 = browser.find_element_by_id('solve').click()
#
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
