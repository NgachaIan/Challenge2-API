import unittest
import os
import sys
import json
import requests
topdir = os.path.join(os.path.dirname(__file__), "../")
sys.path.append(topdir)
from app import create_app

class CreateMeetup(unittest.TestCase):
    def test_create_meetup(self):
        with create_app().test_client() as c:
            url = "/api/version1/meetup/post"
            meetup = {
                "topic": "django",
                "location": "strath",
                "Tags": "pythondjango"
            }
            response = c.post(url, data=json.dumps(meetup), headers={
                              "Content-Type": "application/json"})
            expected = json.loads(response.get_data())
            self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()
