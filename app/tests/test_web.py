# -*- coding: utf-8 -*-
import os
import unittest

from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from app import app, db
from app.models import User, Party


basedir = os.path.abspath(os.path.dirname(__file__))

class test_web(LiveServerTestCase):


    def setUp(self):
        """Setup the test driver and create test users"""
        self.browser = webdriver.PhantomJS()
        self.browser.get(self.get_server_url())

    def tearDown(self):
        self.browser.quit()

    def test_login_selenium(self):
        self.browser.find_element_by_xpath('//*[@id="first_name"]').send_keys('illya')
        self.browser.find_element_by_xpath('//*[@id="last_name"]').send_keys('yurkevich')
        self.browser.find_element_by_xpath('//*[@id="id_number"]').send_keys('320880123')
        self.browser.find_element_by_xpath('//*[@id="EnterBtn"]').send_keys(Keys.ENTER)
        print self.browser.current_url
        assert 'Home' in self.browser.title

    def test_noSuchUser_selenium(self):
        self.browser.find_element_by_xpath('//*[@id="first_name"]').send_keys('no')
        self.browser.find_element_by_xpath('//*[@id="last_name"]').send_keys('such')
        self.browser.find_element_by_xpath('//*[@id="id_number"]').send_keys('user')
        self.browser.find_element_by_xpath('//*[@id="EnterBtn"]').click()
        assert "Flask Intro - login page" in self.browser.title




if __name__ == "__main__":
    unittest.main()
