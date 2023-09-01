from flask import jsonify,make_response
from flask_cors import cross_origin
from flask_restful import Resource
from user.models import User

class UserLogin(Resource):
    def post(self):
        return User().login()

class UserList(Resource):
    def get(self):
        return User().listUsers()

class UserCreate(Resource):
    def post(self):
        return User().createUser()

class UserLogout(Resource):
    def get(self):
        return User().logout()

class UserAccessPilote(Resource):
    def post(self):
        return User().getAccessPilote()

class UserResetPassword(Resource):
    def post(self):
        return User().resetPassword()
    
 




