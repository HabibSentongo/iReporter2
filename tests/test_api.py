import unittest
from flask import json
from api.views.view import app

class TestApi(unittest.TestCase):

    def test_home_api(self):
        # result = app.home_api()
        # self.assertEqual(result,jsonify({'message' : 'Welcome to iReporter!'}))
        self.assertFalse(False)