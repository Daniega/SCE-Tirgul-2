# -*- coding: utf-8 -*-
import unittest

from app import app
from app import db
from db_create import db_create


class myTest(unittest.TestCase):

    def create_app(self):
        return app

    def auth_test(self):
        response = self.tester.get('/secret', content_type='application/json')
        # should return status code 302
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        # Check if form visible
        login_page = self.tester.get('/login')
        assert 'first_name'.encode('utf-8') in login_page.data
        assert 'last_name'.encode('utf-8') in login_page.data
        assert 'id_number'.encode('utf-8') in login_page.data

        # Check if id is missing
        invalid_login = self.tester.post('login', data=dict(first_name='illya', last_name='yurkevich', id_number=''),
                                         follow_redirects=True)
        self.assertEqual(invalid_login.status_code, 404)

        assert 'המצביע אינו מופיע בבסיס הנתונים'.encode('utf-8') in invalid_login.data

    def test_WrongUser(self):
        login_page = self.tester.get('/login')
        assert 'first_name'.encode('utf-8') in login_page.data
        assert 'last_name'.encode('utf-8') in login_page.data
        assert 'id_number'.encode('utf-8') in login_page.data  # check if user exist
        invalid_login = self.tester.post('login', data=dict(first_name='someone', last_name='unknown', id_number='666'),
                                         follow_redirects=True)
        self.assertEqual(invalid_login.status_code, 404)

        assert 'המצביע אינו מופיע בבסיס הנתונים'.encode('utf-8') in invalid_login.data


    def setUp(self):
        self.tester = app.test_client(self)
        db.drop_all()
        db_create(db)
        self.tester.testing = True

    def tearDown(self):
        db.drop_all()
        db.session.remove()


if __name__ == '__main__':
    unittest.main()
