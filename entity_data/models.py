from flask import request, make_response, jsonify

from app.config import dbPerfENERGIE
from app.dbkeys import dataEntityCollection, dbPilotageKey, entityCollection
from entity_data.tableau import TableauData
import json


class EntityData():
    def updateDataEntity(self):
        pass
        # try :
        #
        #     entityId = request.get_json()['entityId']
        #     moisId = request.get_json()['moisId']
        #     rowId = request.get_json()['rowId']
        #     value = request.get_json()['value']
        #     annee = request.get_json()['annee']
        #
        #     datas = databases.get_document(dbPilotageKey, dataEntityCollection, entityId)
        #     dataEntite = TableauData(entityId, datas)
        #     resultUpdate = dataEntite.updateCellData(value,rowId,moisId,annee)
        #
        #     data = {f"data_{annee}": json.dumps(resultUpdate.tolist())}
        #
        #     databases.update_document(dbPilotageKey, dataEntityCollection,entityId,data=data)
        #
        #     return make_response(jsonify("success"), 200)
        #
        # except:
        #     return make_response(jsonify("Impossible de charger les données"), 400)



    # Toutes les donnees d'une entity ( 2022, 2023 etc )
    def getAllDataEntity(self):
        pass
        # try:
        #     entity = request.get_json()['entity']
        #     result = databases.get_document(dbPilotageKey,entityCollection,entity)
        #     datas = databases.get_document(dbPilotageKey, dataEntityCollection, entity)
        #     dataEntite = TableauData(entity,datas)
        #     result["data"] = dataEntite.dataToFlutter()
        #     return make_response(jsonify(result), 200)
        # except:
        #     return make_response(jsonify("Impossible de charger les données"), 400)

    def validateDataEntity(self):
        pass
        # try:
        #     entityId = request.get_json()['entityId']
        #     moisId = request.get_json()['moisId']
        #     rowId = request.get_json()['rowId']
        #     value = request.get_json()['value']
        #     annee = request.get_json()['annee']
        #
        #     datas = databases.get_document(dbPilotageKey, dataEntityCollection, entityId)
        #     dataEntite = TableauData(entityId, datas)
        #     resultUpdate = dataEntite.validateCellData(value, rowId, moisId, annee)
        #
        #     data = {f"validation_{annee}": json.dumps(resultUpdate.tolist())}
        #
        #     databases.update_document(dbPilotageKey, dataEntityCollection, entityId, data=data)
        #
        #     return make_response(jsonify("success"), 200)
        #
        # except:
        #     return make_response(jsonify("Impossible de charger les données"), 400)



