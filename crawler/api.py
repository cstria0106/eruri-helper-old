from flask_cors import CORS
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask

base_url = 'http://eruri.kangwon.ac.kr'

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)

_client: 'Client' = None


class Application(Resource):
    # GET /client
    # 로그인 되어있는 지 확인한다.
    def get(self):
        if _client == None:
            return False

        return _client.logged_in

    # POST /client
    # 로그인한다.
    # 성공하면 OK 전송
    # 실패하면 BAD REQUEST 전송
    def post(self):
        from client import Client
        global _client
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        # UNAUTHORIZED
        _client = Client(args['username'], args['password'])
        if _client.logged_in:
            return {}, 200
        else:
            abort(400)


class Course(Resource):
    # GET /course?id=ID?
    # 전체 과목 혹은 특정 과목 정보를 얻는다.
    # 로그인 되어있지 않다면 UNAUTHORIZED 전송
    # 쿼리에 id가 있고 해당하는 과목이 있다면 해당 과목에 대한 자세한(강의, 과제 정보를 포함한) 정보를 전송
    # 존재하지 않는 과목 id라면 NOT FOUND 전송
    # 쿼리에 id가 없면 모든 과목의 대략적인(강의 ID, 강의명, 교수명을 포함한) 정보 배열을 전송
    def get(self):
        global _client

        # 로그인 되어있지 않다면
        if _client == None:
            abort(401)  # UNAUTHORIZED 전송

        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=False)
        args = parser.parse_args()

        if args['id'] != None:  # id라는 쿼리 문자열이 있는가?
            for course in _client.courses:  # 해당 과목을 과목 목록에서 선형적으로 탐색한다.
                if course.id == args['id']:  # 그 과목이라면
                    return course.serialize(True)  # 그 과목에 자세한 정보를 반환
            return abort(404)  # 찾는 과목이 없다면 NOT FOUND 반환

        # 모든 과목에 대한 대략적인 정보를 반환
        courses = tuple(course.serialize(False) for course in _client.courses)

        return courses


api.add_resource(Application, '/client')
api.add_resource(Course, '/course')
