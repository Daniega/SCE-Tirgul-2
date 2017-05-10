# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver


class test_web(unittest.TestCase):
    def test_login_selenium(self):
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_xpath('//*[@id="first_name"]').send_keys('illya')
        self.browser.find_element_by_xpath('//*[@id="last_name"]').send_keys('yurkevich')
        self.browser.find_element_by_xpath('//*[@id="id_number"]').send_keys('320880123')
        self.browser.find_element_by_xpath('//*[@id="EnterBtn"]').click()
        assert "No results found." not in self.browser.page_source

    def test_noSuchUser_selenium(self):
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_xpath('//*[@id="first_name"]').send_keys('no')
        self.browser.find_element_by_xpath('//*[@id="last_name"]').send_keys('such')
        self.browser.find_element_by_xpath('//*[@id="id_number"]').send_keys('user')
        self.browser.find_element_by_xpath('//*[@id="EnterBtn"]').click()
        assert "Flask Intro - login page" in self.browser.title
        self.assertEqual("Flask Intro - login page", self.browser.title)

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("http://127.0.0.1:5000")



    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
