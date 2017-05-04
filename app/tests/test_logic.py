# -*- coding: utf-8 -*-
import unittest
from app import db
import app
from db_create import db_create


class myTest(unittest.TestCase):
    TESTING = True
    host = '0.0.0.0'

    def auth_test(self):
        response = self.tester.get('/secret', content_type='application/json')
        # should return status code 302
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        # Check if form visible
        login_page = self.tester.get('/login')
        assert 'first_name' in login_page.data
        assert 'last_name' in login_page.data
        assert 'id_number' in login_page.data

        # Check if id is missing
        invalid_login = self.tester.post('login', data=dict(first_name='illya', last_name='yurkevich', id_number=''),
                                         follow_redirects=True)
        assert 'המצביע אינו מופיע בבסיס הנתונים' in invalid_login.data

    def test_WrongUser(self):
        login_page = self.tester.get('/login')
        assert 'first_name' in login_page.data
        assert 'last_name' in login_page.data
        assert 'id_number' in login_page.data  # check if user exist
        invalid_login = self.tester.post('login', data=dict(first_name='someone', last_name='unknown', id_number='666'),
                                         follow_redirects=True)
        assert 'המצביע אינו מופיע בבסיס הנתונים' in invalid_login.data


    def setUp(self):
        self.tester = app.app.test_client(self)
        db.drop_all()
        db_create()



    def tearDown(self):
        db.drop_all()
        db.session.remove()


if __name__ == '__main__':
    unittest.main()
