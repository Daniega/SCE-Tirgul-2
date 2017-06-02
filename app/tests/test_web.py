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
    def create_app(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['LIVESERVER_PORT'] = 8943
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'test.db')  # 'sqlite:///:memory:'
        db.init_app(self.app)
        with self.app.app_context():  # app context
            db.drop_all()
            db.create_all()
            self.populate()

        return self.app

    def populate(self):
        valid_user = User('illya', 'yurkevich','320880123',False)
        valid_party = Party(u'עלה ירוק', 'static/images/yarok.jpeg', 0)
        db.session.add(valid_user)
        db.session.commit()

    def setUp(self):
        """Setup the test driver and create test users"""
        self.browser = webdriver.PhantomJS()
        self.browser.get(self.get_server_url())

    def tearDown(self):
        self.browser.quit()

    def test_login_selenium(self):
        self.valid_user = User('illya', 'yurkevich','320880123',False)
        self.first_name = self.browser.find_element_by_id('first_name')
        self.last_name = self.browser.find_element_by_id('last_name')
        self.id_num = self.browser.find_element_by_id('id_number')
        self.login_button = self.browser.find_element_by_id('EnterBtn')
        self.first_name.send_keys(self.valid_user.first_name)
        self.last_name.send_keys(self.valid_user.last_name)
        self.id_num.send_keys('320880123')
        self.login_button.submit()
        print(self.browser.title)
        assert 'Home' in self.browser.title

    def test_noSuchUser_selenium(self):
        self.browser.find_element_by_xpath('//*[@id="first_name"]').send_keys('no')
        self.browser.find_element_by_xpath('//*[@id="last_name"]').send_keys('such')
        self.browser.find_element_by_xpath('//*[@id="id_number"]').send_keys('user')
        self.browser.find_element_by_xpath('//*[@id="EnterBtn"]').click()
        assert "Flask Intro - login page" in self.browser.title

    def test_full_selenium(self):
        self.valid_user = User('illya', 'yurkevich','320880123',False)
        self.first_name = self.browser.find_element_by_id('first_name')
        self.last_name = self.browser.find_element_by_id('last_name')
        self.id_num = self.browser.find_element_by_id('id_number')
        self.login_button = self.browser.find_element_by_id('EnterBtn')
        self.first_name.send_keys(self.valid_user.first_name)
        self.last_name.send_keys(self.valid_user.last_name)
        self.id_num.send_keys('320880123')
        self.login_button.submit()
        self.browser.implicitly_wait(5)
        print ('here '+self.browser.title)
        self.browser.find_element_by_tag_name('article'[0]).click()
        self.browser.find_element_by_id('btnSubmit').submit()
        alert = self.browser.switchTo().alert();
        alert.accept();
        self.browser.implicitly_wait(5)
        assert "Flask Intro - login page" in self.browser.title





if __name__ == "__main__":
    unittest.main()
