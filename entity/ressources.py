from flask_restful import Resource
from entity.models import Entity


class GetEntityList(Resource):
    def get(self):
        return Entity().listEntity()

class GetEntityById(Resource):
    def get(self,id):
        return Entity().getEntityById(id=id)

class GetEntityByAbr(Resource):
    def get(self,abr):
        return Entity().getEntityByAbr(abr=abr)

#########################################################
class GetEntityPerformanceByYear(Resource):
    def post(self):
        return Entity().getPerformancesEntityByYear()


#########################################################

class GetEntityMonitoring(Resource):
    def post(self):
        return Entity().getSuiviEntity()

class GetEntitesSubMonitoring(Resource):
    def post(self):
        return Entity().getSuiviSubEntity()

class GetEntitesMonitoring(Resource):
    def post(self):
        return Entity().getAllSuiviEntity()

#########################################################

class GetDropDownListQuery(Resource):
    def post(self):
        return Entity().listDropDownEntites()
