
from flask_restful import Api
from flask import Blueprint


from .meetup_views import Meetups
from .question_views import Question
from .question_views import Questions
from .user_views import User

version1 = Blueprint("api", __name__, url_prefix="/api/version1")
api = Api(version1)

api.add_resource(Meetups, '/meetup/post', endpoint='post_meetup')
api.add_resource(Meetups, '/meetup/get', endpoint='get_meetup')
api.add_resource(Meetups, '/meetup/<int:id>', endpoint='delete_meetup')
api.add_resource(Meetups, '/meetup/put', endpoint='put_meetup')
api.add_resource(Question, '/question/post', endpoint='post_question')
api.add_resource(Question, '/question/get', endpoint='get_question')
api.add_resource(Question, '/question/upvote/<int:question_id>',
                 endpoint='upvote_question')
api.add_resource(Questions, '/question/downvote/<int:question_id>',
                 endpoint='downvote_question')
api.add_resource(User, '/user/post', endpoint='post_user')
api.add_resource(User, '/user/get', endpoint='get_user')
