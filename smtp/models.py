from flask import request, make_response

from app.config import dbPerfENERGIE
from smtp.emailing import sendResetPasswordCode
from utils.utils import QueryDocToList


class SendMail:
    def sendResetPassword(self):
        try:
            email = request.get_json()["email"]
            is_user_exit = self.isUserExist(email)
            # print(email)
            if is_user_exit == False:
                return make_response({"message": "Vous n'êtes pas autorisé à effectuer cette réquête.", "status": False},400)

            resultCode = sendResetPasswordCode(email)

            if resultCode["result"] == True:
                return make_response({"message": "Un code code a été envoyé à votre addresse courriel.", "status": True, "code":resultCode["code"]}, 200)

            else:
                return make_response({"message": "La réquête a échoué veuillez réessayer.", "status": False}, 400)

        except :

            return {"message": "La réquête a échoué veuillez réessayer.", "status": False}

    def isUserExist(self,email):
        userCollection = dbPerfENERGIE["users"]
        query = userCollection.find({"email": email})
        users = QueryDocToList(query)
        if len(users) == 1:
            return True
        return False
