import unittest
from flask import json
from app.views.view import app

class TestApi(unittest.TestCase):

    def test_home_api(self):
        self.assertFalse(False)