# -*- coding: utf-8 -*-
import os
import unittest

from flask_testing import LiveServerTestCase
from selenium import webdriver

from app import app, db
from app.models import User, Party


basedir = os.path.abspath(os.path.dirname(__file__))

class test_web(unittest.TestCase):
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
        db.session.commit()
        valid_user = User(111111, 'firstName', 'lastName', False)
        valid_party = Party(u'עלה ירוק', 'static/images/yarok.jpeg', 0)
        db.session.add(valid_party)
        db.session.add(valid_user)
        db.session.commit()

    def setUp(self):
        """Setup the test driver and create test users"""
        self.browser = webdriver.PhantomJS()
        self.browser.get('http://127.0.0.1:5000/login?next=%2F')

    def tearDown(self):
        self.browser.quit()

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




if __name__ == "__main__":
    unittest.main()
