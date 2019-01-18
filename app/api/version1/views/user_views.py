from flask import Flask, make_response, jsonify
from flask_restful import fields, marshal, Resource, Api, reqparse


import datetime

app = Flask(__name__)
api = Api(app)

users = []

user_fields = {
    "id": fields.Integer,
    "firstname": fields.String,
    "lastname": fields.String,
    "othername": fields.String,
    "email": fields.String,
    "phoneNumber": fields.String,
    "username": fields.String,
    "registered": fields.DateTime,
    "isAdmin": fields.Boolean,
    "password": fields.String
}


class User(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.datetime = datetime.datetime.utcnow()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('firstname', type=str, location='json')
        self.reqparse.add_argument('lastname', type=str, location='json')
        self.reqparse.add_argument('othername', type=str, location='json')
        self.reqparse.add_argument('email', type=str, location='json')
        self.reqparse.add_argument('phoneNumber', type=str, location='json')
        self.reqparse.add_argument('username', type=str, location='json')
        self.reqparse.add_argument(
            'registered', type=datetime, location='json')
        self.reqparse.add_argument('isAdmin', type=bool, location='json')
        self.reqparse.add_argument('password', type=str, location='json')
        super(User, self).__init__

    def get(self):
        return {'users': [marshal(user, user_fields) for user in users]}

    def post(self):
        required = self.reqparse.parse_args(strict=True)
        args = self.reqparse.parse_args()
        user = {
            'firstname': args['firstname'],
            'lastname': args['lastname'],
            'othername': args['othername'],
            'email': args['email'],
            'phoneNumber': args['phoneNumber'],
            'username': args['username'],
            'registered': self.datetime,
            'isAdmin': False,
            'id': len(users)

        }
        if not required['firstname']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The firstname field is required"}), 400)

        if not required['lastname']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The lastname field is required"}), 400)

        if not required['othername']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The othername field is required"}), 400)

        if not required['email']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The email field is required"}), 400)

        if not required['phoneNumber']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The phoneNumber field is required"}), 400)

        else:
            users.append(user)
            return {'user': marshal(user, user_fields)}, 201
