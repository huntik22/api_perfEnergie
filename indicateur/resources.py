from flask import jsonify,make_response
from flask_restful import Resource

from indicateur.models import Indicateur
from user.models import User


class IndicateurList(Resource):
    def get(self):
        return Indicateur().listIndicateurs()
    


