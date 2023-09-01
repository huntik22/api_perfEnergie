from flask import Flask, make_response, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin

from entity.ressources import *
from entity_data.ressources import *
from indicateur.resources import IndicateurList
from smtp.resources import SendResetPasswordCode
from tableau_bord.resources import getCritereList, getIndicateurList
from user.resources import UserLogin, UserCreate, UserLogout, UserList, UserAccessPilote, UserResetPassword

app = Flask(__name__)
CORS(app,origins="*",allow_headers=['Content- Type','Authorization'])
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"status":True}



api.add_resource(HelloWorld, '/')
api.add_resource(UserLogin, '/user/login') # Login
api.add_resource(UserCreate, '/user/create') # Create user
api.add_resource(UserLogout, '/user/logout') # Logout User
api.add_resource(UserList, '/user/list') # Logout User
api.add_resource(UserAccessPilote, '/user/accespilote')
api.add_resource(UserResetPassword, '/user/reset-password')
api.add_resource(SendResetPasswordCode, '/user/forgot-password')


api.add_resource(IndicateurList, '/indicateur/list')


api.add_resource(GetEntityList, '/entity/list')
api.add_resource(GetEntityById, '/entity/id/<string:id>')
api.add_resource(GetEntityByAbr, '/entity/abr/<string:abr>')


api.add_resource(GetEntityPerformanceByYear, '/entity/performs/year')

api.add_resource(GetDropDownListQuery, '/entity/params')

#api.add_resource(GetEntitesMonitoring, '/entity/monitoring/list/all')
api.add_resource(GetEntityMonitoring, '/entity/monitoring/year')
api.add_resource(GetEntitesSubMonitoring, '/entity/monitoring/partial')
api.add_resource(GetEntitesMonitoring, '/entity/monitoring/all')


api.add_resource(GetDataEnity, '/dataentity/all')
api.add_resource(UpdateDataEntity,'/dataentity/update/cell')
api.add_resource(ValidateDataEntity,'/dataentity/validate/cell')


api.add_resource(getCritereList,"/critere/getlist")
api.add_resource(getIndicateurList,"/indicateur/getlist")
#api.add_resource(EntityList, '/entity/data')
#api.add_resource(SendEmailCreation,'/mail/creationAccount')


if __name__ == '__main__':
    app.run(debug=False)
    
