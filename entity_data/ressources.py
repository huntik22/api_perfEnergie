from flask_restful import Resource

from entity_data.models import EntityData

class GetDataEnity(Resource):
    def post(self):
        return EntityData().getAllDataEntity()

class UpdateDataEntity(Resource):
    def post(self):
        return EntityData().updateDataEntity()

class ValidateDataEntity(Resource):
    def post(self):
        return EntityData().validateDataEntity()



