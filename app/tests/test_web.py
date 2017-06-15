import os
import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask import Flask
from flask_testing import LiveServerTestCase
from app.models import User, Party
from app import app , db




class SeleniumTest(LiveServerTestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 10
        db.init_app(app)
        with app.app_context():
            db.create_all()
            self.init_db()
        return app

    def init_db(self):
        db.session.commit()
        u = User('illya', 'yurkevich', '123')
        likud = Party(u'הליכוד','https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Likud_Logo.svg/250px-Likud_Logo.svg.png')
        db.session.add(u)
        db.session.add(likud)
        db.session.commit()
 ##
    def setUp(self):
        # create a new Firefox session
         self.browser = webdriver.PhantomJS()
         # nevigate to the application home page
         self.browser.get(self.get_server_url())
         self.str = 'המצביע אינו מופיע בבסיס הנתונים או שכבר הצביע'

    def test_correct_details(self):
        ################# Get In with correct details #################
        first_name_Input = self.browser.find_element_by_id("first_name")
        first_name_Input.send_keys("illya")
        last_name_Input = self.browser.find_element_by_id("last_name")
        last_name_Input.send_keys("yurkevich")
        id_Input = self.browser.find_element_by_id("id_number")
        id_Input.send_keys("123")
        id_Input.send_keys(Keys.ENTER)
        assert self.str not in self.browser.page_source

        #browser.save_screenshot('correctDatails.png')

    def test_incorrect_details(self):
        ################# Try to Get In with incorrect details ##########
        first_name_Input = self.browser.find_element_by_id("first_name")
        first_name_Input.send_keys("dani")
        last_name_Input = self.browser.find_element_by_id("last_name")
        last_name_Input.send_keys("shapi")
        id_Input = self.browser.find_element_by_id("id_number")
        id_Input.send_keys("111")
        id_Input.send_keys(Keys.ENTER)
        assert self.str in self.browser.page_source
        #browser.save_screenshot('incorrectDatails.png')
        #################################################################

    def test_full_check(self):
        first_name_Input = self.browser.find_element_by_id("first_name")
        first_name_Input.send_keys("illya")
        last_name_Input = self.browser.find_element_by_id("last_name")
        last_name_Input.send_keys("yurkevich")
        id_Input = self.browser.find_element_by_id("id_number")
        id_Input.send_keys("123")
        id_Input.send_keys(Keys.ENTER)
        select = self.browser.find_element_by_id("הליכוד")
        select.send_keys(Keys.ENTER)
        done_btn = self.browser.find_element_by_id("('EnterBtn')")
        done_btn.send_keys(Keys.ENTER)
        Keys.ENTER
        assert "ברוכים הבאים" in self.browser.page_source



    def tearDown(self):
        self.browser.quit()
        with app.app_context():
            db.drop_all()
            db.session.remove()

if __name__ == '__main__':
    unittest.main()