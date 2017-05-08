# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from app.tests import app


class test_web(unittest.TestCase):

    def test_login_selenium(self):
        self.browser.find_element_by_xpath('//*[@id="first_name"]').send_keys('illya')
        self.browser.find_element_by_xpath('//*[@id="last_name"]').send_keys('yurkevich')
        self.browser.find_element_by_xpath('//*[@id="id_number"]').send_keys('320880123')
        self.browser.find_element_by_xpath('//*[@id="EnterBtn"]').click()
        assert "No results found." not in self.browser.page_source

    def test_noSuchUser_selenium(self):
        self.browser.find_element_by_xpath('//*[@id="first_name"]').send_keys('no')
        self.browser.find_element_by_xpath('//*[@id="last_name"]').send_keys('such')
        self.browser.find_element_by_xpath('//*[@id="id_number"]').send_keys('user')
        self.browser.find_element_by_xpath('//*[@id="EnterBtn"]').click()
        assert u'המצביע אינו מופיע בבסיס הנתונים' in self.browser.page_source



    def setUp(self):
        self.tester = app.test_client(self)
        self.tester.testing = True
        # some ****ing problem with chromedriver
        self.browser = webdriver.Edge()

        self.browser.get('http://localhost:5000/')

    def tearDown(self):
        self.browser.quit()



if __name__ == "__main__":
    unittest.main()
