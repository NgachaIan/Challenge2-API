import unittest
import os
import sys
import json
import requests
topdir = os.path.join(os.path.dirname(__file__), "../")
sys.path.append(topdir)
from app import create_app


class CreateUser(unittest.TestCase):
    def test_create_user(self):
        with create_app().test_client() as c:
            url = "/api/version1/user/post"
            user = {
                "firstname": "ian",
                "lastname": "ngacha",
                "othername": "duncan",
                "email": "ngachaian@gmail.com",
                "phoneNumber": "0723424223",
                "username": "iano",
                "isAdmin": False

            }
            response = c.post(url, data=json.dumps(user), headers={
                              "Content-Type": "application/json"})
            expected = json.loads(response.get_data())
            self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()
