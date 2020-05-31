from flask_cors import CORS
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask

base_url = 'http://eruri.kangwon.ac.kr'


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)

_client: 'Client' = None


class Application(Resource):
    def get(self):
        if _client == None:
            return False

        return _client.logged_in

    def post(self):
        from client import Client
        global _client
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        _client = Client(args['username'], args['password'])
        if _client.logged_in:
            return {}, 200
        else:
            abort(400)


class Course(Resource):
    def get(self):
        global _client
        if _client == None:
            abort(401)

        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=False)
        args = parser.parse_args()

        if args['id'] != None:
            for course in _client.courses:
                if course.id == args['id']:
                    return course.serialize(True)
            return abort(404)

        courses = tuple(course.serialize(False) for course in _client.courses)

        return courses


api.add_resource(Application, '/client')
api.add_resource(Course, '/course')
