import unittest
import pytest
from selenium.webdriver.support.ui import WebDriverWait as WWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math


keke = []


@pytest.mark.parametrize('link', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_something(browser, link):
    links = f"https://stepik.org/lesson/236{link}/step/1"
    browser.get(links)
    ans = WWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "ember-text-area.ember-view.textarea"
                                                                              ".string-quiz__textarea")))
    ans.click()
    ans.send_keys(str((math.log(int(time.time())))))
    send = browser.find_element_by_class_name("submit-submission").click()
    global keke
    if WWait(browser, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "smart-hints__hint"), 'Correct!')):
        return True
    else:
        not_right = browser.find_element_by_class_name("smart-hints__hint")
        keke.append(not_right.text)
        return keke


if __name__ == '__main__':
    unittest.main()
