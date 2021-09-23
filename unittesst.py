import time
import unittest
import anyway


class Logins(unittest.TestCase):

    # def test_search(self):
    #     result = anyway.search()
    #     self.assertEquals('Cool', result)

    def test_login(self):
        result = anyway.login('nnamnam360+8@gmail.com', 'qwer1234A!')
        self.assertEquals('Test passed', result)

    def test_logout(self):
        res = anyway.log_out()
        self.assertEquals('Test passed', res)

    def test_login_failed(self):
        result = anyway.login('nnamnam360+7@gmail.com', 'qwer1234A!')
        self.assertEquals("Login failed", result)
