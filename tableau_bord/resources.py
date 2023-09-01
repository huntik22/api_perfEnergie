from flask import jsonify,make_response
from flask_restful import Resource

from tableau_bord.models import Indicateur,Critere
from user.models import User


class getIndicateurList(Resource):
    def post(self):
        return Indicateur().listIndicateurs()
    
class getCritereList(Resource):
    def get(self):
        return Critere().listCritere()

# class addAxeInd(Resource):
#     def get(self):
#         return add_axe().addAxeIndicator()