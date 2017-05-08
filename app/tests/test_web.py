# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


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
        self.browser = webdriver.Remote("http://127.0.1.0:5000/wd/hub", desired_capabilities= {
          "browserName": "chrome",
          "maxInstances": 1,
          "seleniumProtocol": "WebDriver"
        })
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
