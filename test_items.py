import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as WWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_basket_button(browser):
    links = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(links)
    try:
        cock = WWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to"
                                                                                  "-basket")))
        assert cock is not None
    except TimeoutException:
        raise TimeoutException("Button was not found for 5 second")


if __name__ == '__main__':
    pytest.main()
