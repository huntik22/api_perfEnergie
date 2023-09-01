from flask_restful import Resource

from smtp.models import SendMail


class SendResetPasswordCode(Resource):
    def post(self):
        return SendMail().sendResetPassword()