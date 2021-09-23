import time
from selenium.webdriver.chrome.webdriver import WebDriver

# browser = WebDriver()
#
#
# def search():
#     browser.get(
#         'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
#     res = browser.find_element_by_id('n-mainpage-description')
#     if res is not None and res != '':
#         return "Cool"
#
#
# def login(user_cred, password_cred):
#     browser.get('https://preprod_test:dkuFGd8BXJ2UiVmJiQs@professionals-p3.preprod.curamedon.com/en/login')
#     user = browser.find_element_by_name('userName')
#     user.send_keys(user_cred)
#     password = browser.find_element_by_name('password')
#     password.send_keys(password_cred)
#     time.sleep(1)
#     password.send_keys('\ue007')
#     time.sleep(2)
#     sms = browser.find_element_by_name('smsCode')
#     sms.send_keys('1111' + '\ue007')
#     time.sleep(2)
#     res = browser.find_element_by_name('date-picker')
#     if res is not None:
#         return "Test passed"
#     else:
#         return "Login failed"
#
#
# def log_out():
#     browser.get('https://professionals-p3.preprod.curamedon.com/logout')
#     time.sleep(2)
#     ok = browser.find_element_by_name('userName')
#     if ok is not None or ok != '':
#         return "Test passed"
#     time.sleep(3)


def make_link():
    nums = range(5, 10)
    links = []
    yield
    for num in nums:
        link = f"https://stepik.org/lesson/23689{num}/step/1"
        links.append(link)
        print(links)
    return print(links)

# browser.get('http://suninjuly.github.io/find_xpath_form')
# name = browser.find_element_by_name('first_name')
# name.send_keys('Ivan')
# last = browser.find_element_by_name('last_name')
# last.send_keys('Petrov')
# city = browser.find_element_by_class_name('city')
# city.send_keys('Smolensk')
# country = browser.find_element_by_id('country')
# country.send_keys('Russia')
# button = browser.find_element_by_xpath('/html/body/div/form/div[6]/button[3]')
# button.click()
# time.sleep(15)
# browser.quit()
# browser.close()

for i in make_link():
    print(i)


