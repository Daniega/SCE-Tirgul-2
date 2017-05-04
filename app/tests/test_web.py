# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import os

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
        # some ****ing problem with chromedriver
        chromedriver = "/Users/illya/Downloads/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.get('http://localhost:5000/')

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
