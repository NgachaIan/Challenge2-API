from flask_restful import fields, marshal, Resource, Api, reqparse
import datetime
from flask import Flask, jsonify, make_response, request, abort

meetups = []

meetup_fields = {
    "id": fields.Integer,
    "createdOn": fields.DateTime,
    "location": fields.String,
    "topic": fields.String,
    "happeningOn": fields.DateTime,
    "Tags": fields.String,
}


class Meetups(Resource):
    def __init__(self):
        self.datetime = datetime.datetime.utcnow()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')
        self.reqparse.add_argument('createdOn', type=datetime, location='json')
        self.reqparse.add_argument('location', type=str, location='json')
        self.reqparse.add_argument('topic', type=str, location='json')
        self.reqparse.add_argument(
            'happeningOn', type=datetime, location='json')
        self.reqparse.add_argument('Tags', type=str, location='json')
        super(Meetups, self).__init__

    def post(self):
        args = self.reqparse.parse_args()
        meetup = {
            'createdOn': self.datetime,
            'topic': args['topic'],
            'location': args['location'],
            'Tags': args['Tags'],
            'id': len(meetups)
        }

    def get(self):
        return {'meetups': [marshal(meetup, meetup_fields) for meetup in meetups]}
