# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



class test_web(unittest.TestCase):
    def test_login_selenium(self):
        self.browser.find_element_by_xpath('//*[@id="first_name"]').send_keys('illya')
        self.browser.find_element_by_xpath('//*[@id="last_name"]').send_keys('yurkevich')
        self.browser.find_element_by_xpath('//*[@id="id_number"]').send_keys('320880123')
        self.browser.find_element_by_xpath('//*[@id="EnterBtn"]').send_keys(Keys.ENTER)
        print self.browser.current_url
        self.assertEqual('http://127.0.0.1:5000/login?next=%2F', self.browser.current_url)

    def test_noSuchUser_selenium(self):
        self.browser.find_element_by_xpath('//*[@id="first_name"]').send_keys('no')
        self.browser.find_element_by_xpath('//*[@id="last_name"]').send_keys('such')
        self.browser.find_element_by_xpath('//*[@id="id_number"]').send_keys('user')
        self.browser.find_element_by_xpath('//*[@id="EnterBtn"]').click()
        assert "Flask Intro - login page" in self.browser.title

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.get("http://127.0.0.1:5000/login?next=%2F")




    def tearDown(self):
        self.browser.quit()



if __name__ == "__main__":
    unittest.main()
