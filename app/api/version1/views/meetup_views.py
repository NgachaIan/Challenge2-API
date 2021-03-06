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
        required = self.reqparse.parse_args(strict=True)
        args = self.reqparse.parse_args()
        meetup = {
            'createdOn': self.datetime,
            'topic': args['topic'],
            'location': args['location'],
            'Tags': args['Tags'],
            'id': len(meetups)
        }
        if not required['createdOn']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The created on field is required"}), 400)

        if not required['topic']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The topic field is required"}), 400)

        if not required['location']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The location field is required"}), 400)

        if not required['Tags']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The Tags field is required"}), 400)

        else:
            meetups.append(meetup)
            return {'meetup': marshal(meetup, meetup_fields)}, 201

    def put(self):
        args = self.reqparse.parse_args()
        meetup = {
            'createdOn': self.datetime,
            'topic': args['topic'],
            'location': args['location'],
            'Tags': args['Tags']
        }
        return {'meetup': marshal(meetup, meetup_fields)}, 200

    def delete(self, id):

        meetup = [meetup for meetup in meetups if meetup['id'] == id]
        if len(meetup) == 0:
            abort(404)

        meetups.remove(meetup[0])
        return make_response(jsonify({"status": 200, "data": meetups}), 200)

    def get(self):

        return {'meetups': [marshal(meetup, meetup_fields) for meetup in meetups]}
