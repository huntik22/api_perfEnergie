from appwrite.query import Query
from flask import request, jsonify, make_response
from datetime import datetime
from constants.data_json import getPerfByName, annees, listPiliers, listEnjeux, entitesSub, entitesId, entiteName
from app.dbkeys import *
from app.config import dbPerfENERGIE


class Entity():
    
    def listEntity(self):
        try:
            entites = dbPerfENERGIE.list_documents(entityCollection, limit=100)
            return make_response(jsonify(entites), 200)
        except:
            return make_response(jsonify("Impossible de charger les données"), 400)

    def getEntityByAbr(self, abr):
        try:
            entites = dbPerfENERGIE.list_documents(entityCollection, queries=[Query.equal("enity_abr", abr)])["documents"]
            if len(entites) == 1:
                return make_response(jsonify(entites[0]), 200)
            else:
                return make_response(jsonify("Impossible de charger les données"), 400)
        except:
            return make_response(jsonify("Impossible de charger les données"), 400)

    def getEntityById(self, id):
        try:
            entite = dbPerfENERGIE.get_document(entityCollection, id)
            return make_response(jsonify(entite), 200)
        except:
            return make_response(jsonify("Impossible de charger les données"), 400)

    def entityById(id):
        entite = dbPerfENERGIE.get_document(entityCollection, id)
        return jsonify(entite)

############################################################"

    def getPerformancesEntityByYear(self):
        pass
        # try:
        #     annee = request.get_json()['annee']
        #     entityId = request.get_json()['entity']
        #
        #     resultAnneeN = databases.get_document(dbPilotageKey,performanceCollection,f"{entityId}_{annee}")
        #
        #     dataPilierAnneeN = [resultAnneeN["perf_pilier1"],resultAnneeN["perf_pilier2"],
        #                         resultAnneeN["perf_pilier3"],resultAnneeN["perf_pilier4"]]
        #
        #
        #     dataEnjeuAnneeN = [resultAnneeN["perf_enjeu1a"],resultAnneeN["perf_enjeu1b"],resultAnneeN["perf_enjeu2"],resultAnneeN["perf_enjeu3"],
        #                        resultAnneeN["perf_enjeu4"],resultAnneeN["perf_enjeu5"],resultAnneeN["perf_enjeu6"],resultAnneeN["perf_enjeu7"],
        #                        resultAnneeN["perf_enjeu8"],resultAnneeN["perf_enjeu9"],resultAnneeN["perf_enjeu10"]]
        #
        #     if annee-1 in annees:
        #
        #         resultAnneeN1 = databases.get_document(dbPilotageKey,performanceCollection, f"{entityId}_{annee-1}")
        #         dataPilierAnneeN1 = [resultAnneeN1["perf_pilier1"],resultAnneeN1["perf_pilier2"],
        #                         resultAnneeN1["perf_pilier3"],resultAnneeN1["perf_pilier4"]]
        #         dataEnjeuAnneeN1 = [resultAnneeN1["perf_enjeu1a"],resultAnneeN1["perf_enjeu1b"],resultAnneeN1["perf_enjeu2"],resultAnneeN1["perf_enjeu3"],
        #                        resultAnneeN1["perf_enjeu4"],resultAnneeN1["perf_enjeu5"],resultAnneeN1["perf_enjeu6"],resultAnneeN1["perf_enjeu7"],
        #                        resultAnneeN1["perf_enjeu8"],resultAnneeN1["perf_enjeu9"],resultAnneeN1["perf_enjeu10"],]
        #     else:
        #         dataPilierAnneeN1 = [0,0,0,0]
        #         dataEnjeuAnneeN1 = [0, 0, 0, 0,0, 0, 0, 0,0, 0]
        #
        #
        #     result = {
        #         "nom_entite": resultAnneeN["nom_entity"],
        #         "anneeN": annee,
        #         "performance_pilier": {
        #             "piliers": listPiliers,
        #             "anneeN": dataPilierAnneeN,
        #             "anneeN1": dataPilierAnneeN1
        #         },
        #         "performance_enjeux": {
        #             "enjeux": listEnjeux,
        #             "anneeN": dataEnjeuAnneeN,
        #             "anneeN1": dataEnjeuAnneeN1
        #         }
        #     }
        #
        #     return make_response(jsonify(result), 200)
        # except:
        #     return make_response(jsonify("Impossible de charger les données"), 400)

##################################################################

    def getSuiviEntity(self):
        pass
        # try:
        #     entity = request.get_json()['entity']
        #     annee = request.get_json()['annee']
        #     idSuivi = f"{entity}_{annee}"
        #     result = databases.get_document(dbPilotageKey,monitoringCollection,idSuivi)
        #     return make_response(jsonify(result), 200)
        # except:
        #     return make_response(jsonify("Impossible de charger les données"), 400)

    def getAllSuiviEntity(self):
        pass
        # try:
        #     entity = request.get_json()['entity']
        #     sub_entity = entitesSub[entitesId.index(entity)]
        #     annee = request.get_json()['annee']
        #     result = databases.list_documents(dbPilotageKey,monitoringCollection)
        #     jsonResult = {"documents":[],"total":0}
        #     for doc in result["documents"]:
        #         if doc["annee"] == annee :
        #             jsonResult["documents"].append(doc)
        #     jsonResult["total"] = len(jsonResult["documents"])
        #     return make_response(jsonify(jsonResult), 200)
        # except:
        #     return make_response(jsonify("Impossible de charger les données"), 400)

    def getSuiviSubEntity(self):
        pass
        # try:
        #     entity = request.get_json()['entity']
        #     sub_entity = entitesSub[entitesId.index(entity)]
        #     annee = request.get_json()['annee']
        #     result = databases.list_documents(dbPilotageKey,monitoringCollection,queries=[Query.search("entity",sub_entity)])
        #     jsonResult = {"documents":[],"total":0}
        #     for doc in result["documents"]:
        #         if doc["annee"] == annee :
        #             jsonResult["documents"].append(doc)
        #     jsonResult["total"] = len(jsonResult["documents"])
        #     return make_response(jsonify(jsonResult), 200)
        # except:
        #     return make_response(jsonify("Impossible de charger les données"), 400)

######################################################################

    def listDropDownEntites(self):
        pass
        # try:
        #
        #     entityId = request.get_json()["entityId"]
        #     entitySub = entitesSub[entitesId.index(entityId)]
        #
        #     dataResult = {
        #         "palmci":{
        #             "entitesId": ["palmci", "palmci_siege", "palmci_ehania", "palmci_iboke"],
        #             "entitesAbr": ["plmci", "plmci_siege", "plmci_ehnia", "plmci_iboke"],
        #             "entitesName": ['PALMCI', 'Palmci Siège', 'Palmci Ehania', 'Palmci Iboké'],
        #         },
        #         "sucrivoire": {
        #             "entitesId": ["sucrivoire", "sucrivoire_siege","sucrivoire_borotou_koro", "sucrivoire_zuenoula"],
        #             "entitesAbr": ["scriv", "scriv_siege","scriv_btkr", "scriv_znla"],
        #             "entitesName": ['SUCRIVOIRE', 'Sucrivoire Siège', 'Sucrivoire Borotou-Koro', 'Sucrivoire Zuénoula'],
        #         },
        #     }
        #
        #     result = {
        #         "primaryEntity":entiteName[entitesId.index(entityId)],
        #         "annees": annees,
        #         "currentMonth":datetime.now().month,
        #         "currentAnnee": datetime.now().year
        #     }
        #
        #     result.update(dataResult[entitySub])
        #
        #     return make_response(jsonify(result), 200)
        # except:
        #     return make_response(jsonify("Impossible de charger les données"), 400)