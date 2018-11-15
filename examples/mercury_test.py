from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_basic(self):
        self.open('http://newtours.demoaut.com/')
        self.assert_element('img[alt="Featured Destination: Aruba"]')
        self.send_keys('input[name="userName"]', 'mercury')
        self.send_keys('input[name="password"]', 'mercury')
        self.click('input[name="login"]')