import unittest
import os
import sys
import json
import requests
topdir = os.path.join(os.path.dirname(__file__), "../")
sys.path.append(topdir)
from app import create_app


class CreateQuestion(unittest.TestCase):
    def test_create_meetup(self):
        with create_app().test_client() as c:
            url = "/api/version1/question/post"
            question = {
                "createdBy": 1,
                "meetup": 2,
                "title": "python-django",
                "body": "what is django?",
                "votes": 2

            }
            response = c.post(url, data=json.dumps(question), headers={
                              "Content-Type": "application/json"})
            expected = json.loads(response.get_data())
            self.assertEqual(response.status_code, 201)
