from math import ceil
from appwrite.query import Query
from utils.utils import QueryDocToList
from app.config import dbPerfENERGIE
from flask import jsonify, make_response,request
from app.dbkeys import indicateurCollection,dbPilotageKey
#import smartsheet


class Indicateur:

    def listIndicateurs(self):
        indicatorList=[]
        # reference=request.get_json()["reference"]
        annee=request.get_json()["annee"]
        indicateur_Collection=dbPerfENERGIE["indicateurs"]
        tb_data_Collection=dbPerfENERGIE["indDataTB"]   
        list_data_tb=tb_data_Collection.find({"annee":annee})
        list_indicateur=indicateur_Collection.find()
        list_indicateur=[indicateur for indicateur in list_indicateur]
        list_data_tb=[tb_data for tb_data in list_data_tb]
        if len(list_indicateur) and len(list_data_tb) == 0 or len(list_indicateur)==0 or len(list_data_tb)==0:
                response_data = {"statut": False, "message": "Un Problème est survenu lors du Chargement des Indicateurs"}
                return make_response(jsonify(response_data), 400)
        print( list_indicateur)
        for i in range(len(list_indicateur)):
                list_indicateur[i]['_id'] = str(list_indicateur[i]['_id'])
                # if list_indicateur[i]['processus']!="aucun":
                # process=list_indicateur[i]["processus"].split("\n")               
                list_indicateur[i]["processus"]=str(list_indicateur[i]["processus"]).split("\n")
                
       
        for i in range(0,len(list_data_tb)):
            list_data_tb[i]['_id'] = str(list_data_tb[i]['_id'])
            for j in range(0,len(list_indicateur)):
                if( list_indicateur[j]['idIndicateur']==list_data_tb[i]['idIndicateur']):
                        list_indicateur[j]['realise']=list_data_tb[i]['realise']
                        Mois=["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
                        for mois in Mois :
                            list_indicateur[j][mois]=list_data_tb[i][mois]
        
        return make_response(jsonify(list_indicateur),200)
            
       
    def updateIndicateur(self):
        pass
    def deleteIndicateur(self):
        pass
    def createIndicateur(self):
        pass
    
class Critere: 
    
    def listCritere(self):
        critere_collection = dbPerfENERGIE["critere_energ"]
        list_critere = critere_collection.find({}, {})
        
        # Convertir l'objet Cursor en une liste de dictionnaires
        critere_list = [critere for critere in list_critere]
        
        if len(critere_list) == 0:
            response_data = {"statut": False, "message": "Un Problème est survenu lors du Chargement des Critères"}
            return make_response(jsonify(response_data), 400)
        for i in range(0,len(critere_list)):
            critere_list[i]['_id'] = str(critere_list[i]['_id'])
        return make_response(jsonify(critere_list), 200)
            
        


# class add_axe:
#         def addAxeIndicator(self):
#                 enjeuCollection=dbPerfQSE["Enjeu"]
#                 indicateurCollection=dbPerfQSE["Indicator"]
#                 enjeu=QueryDocToList(enjeuCollection.find())
#                 indicateur=QueryDocToList(indicateurCollection.find())
                
#                 for i in range(0,len(indicateur)):
#                     for j in range(0,len(enjeu)):
#                         if enjeu[j]["libelle"]== indicateur[i]["enjeu"]:
#                             indicateurCollection.update_one({"numero":indicateur[i]["numero"]},{"$set": {"id_axe":enjeu[j]["id_axe"]}})
#                 return make_response({"status": True, "message": "effectue"}, 200)
