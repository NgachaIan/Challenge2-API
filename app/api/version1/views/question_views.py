from flask import Flask, jsonify, make_response
from flask_restful import fields, marshal, Resource, Api, reqparse


from datetime import datetime
import json
from json import dumps

app = Flask(__name__)
api = Api(app)

questions = []


question_fields = {
    "id": fields.Integer,
    "createdBy": fields.Integer,
    "meetup": fields.Integer,
    "title": fields.String,
    "body": fields.String,
    "votes": fields.Integer,
}


class Question(Resource):
    def __init__(self):
        self.datetime = datetime.now()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')
        self.reqparse.add_argument('createdBy', type=int, location='json')
        self.reqparse.add_argument('meetup', type=int, location='json')
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('body', type=str, location='json')
        self.reqparse.add_argument('votes', type=int, location='json')
        super(Question, self).__init__

    def post(self):
        required = self.reqparse.parse_args(strict=True)
        args = self.reqparse.parse_args()
        question = {
            'createdBy': args['createdBy'],
            'meetup': args['meetup'],
            'title': args['title'],
            'body': args['body'],
            'votes': args['votes'],
            'id': len(questions)
        }
        if not required['createdBy']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The createdBy field is required"}), 400)

        if not required['meetup']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The meetup field is required"}), 400)

        if not required['title']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The title field is required"}), 400)

        if not required['body']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The body field is required"}), 400)

        if not required['votes']:
            return make_response(jsonify({"status": 400,
                                          "Error": "The votes field is required"}), 400)

        else:
            questions.append(question)
            return {'question': marshal(question, question_fields)}, 201

    def patch(self, question_id):
        args = self.reqparse.parse_args()
        self.reqparse.add_argument('votes', type=int, location='json')
        question = {
            'createdBy': args['createdBy'],
            'meetup': args['meetup'],
            'title': args['title'],
            'body': args['body'],
            'votes': args['votes']
        }
        for question in questions:
            if question['id'] == question_id:
                question['votes'] = args['votes'] + 1
                return question

        return jsonify({'question': marshal(question, question_fields)}), 200

    def get(self):
        return {'questions': [marshal(question, question_fields) for question in questions]}


class Questions(Question):
    def patch(self, question_id):
        args = self.reqparse.parse_args()
        self.reqparse.add_argument('votes', type=int, location='json')
        question = {
            'createdBy': args['createdBy'],
            'meetup': args['meetup'],
            'title': args['title'],
            'body': args['body'],
            'votes': args['votes']
        }
        for question in questions:
            if question['id'] == question_id:
                question['votes'] = args['votes'] - 1
                return question

        return jsonify({'question': marshal(question, question_fields)}), 200
