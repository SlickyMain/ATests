import unittest
import drop_to
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.chrome()
    yield browser
    browser.quit()


class TestByPytest(unittest.TestCase):
    # def test_reg(self):
    #     result = drop_to.reg('http://suninjuly.github.io/registration2.html', 'First', 'Last', 'Email')
    #     self.assertEqual(True, result)
    #
    # def test_reg2(self):
    #     result = drop_to.reg('http://suninjuly.github.io/registration1.html', 'First', 'Last', 'Email')
    #     self.assertEqual(True, result)
    @pytest.mark.xfail(strict=True)
    def test_succeed(self):
        assert True

    @pytest.mark.xfail
    def test_not_succeed(self):
        assert False

    @pytest.mark.skip
    def test_skipped(self):
        assert False


if __name__ == '__main__':
    unittest.main()
