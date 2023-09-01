from flask import request, jsonify, make_response
from app.config import myclient, dbPerfENERGIE
from utils.utils import QueryDocToList

class User:

    def login(self):
        try:
            email = request.get_json()["email"]
            password = request.get_json()["password"]
            userDoc = self.getUserDocByEmail(email)
            if userDoc == None:
                return make_response({"status": "failed", "message": "User not exit"}, 400)
            if password != userDoc["password"]:  # Ici on va comparer les hash_password
                return make_response({"status": "failed", "message": "Mot de passe incorrect"}, 400)

            del userDoc["password"]
 
            return make_response(userDoc, 200)

        except :
            return make_response({"status": "failed", "message": "La réquête a échoué."}, 400)

    def logout(self):
        return make_response(jsonify({"status": "logout"}), 200)

    def getAccessPilote(self):
        pass

    def getAccesPilotageData(self, id):
        pass

    def createUser(self):
        pass
        # try:
        #     data = request.get_json()['data']
        #     email = data['email']
        #     password = data['password']
        #     name = data['name']
        #     lastName = data['lastName']
        #     nomEntite = data['entity']
        #     fonction = data['fonction']
        #     contact = data['contacts']
        #     adresse = data['address']
        #     acces = data['acces']
        #
        #
        #     if self.getUserIdByEmail(email) != None:
        #         return make_response(jsonify("Cet utilisateur existe déjà dans la base de données"), 455)
        #
        #     accesCreateDoc = {
        #         "email": email,
        #         "entite_primaire": entitesId[entiteName.index(nomEntite)],
        #         "processus_entite": "all",
        #         "est_validateur": "Validateur" in acces,
        #         "est_spectateur": "Spectateur" in acces,
        #         "est_collecteur": "Collecteur" in acces
        #     }
        #
        #     accesId = "".join(email.split("@"))
        #     databases.create_document(dbPilotageKey,accesPilotageCollection, accesId, accesCreateDoc)
        #
        #     userCreateDoc = {
        #         "email": email,
        #         "nom": name,
        #         "prenom": lastName,
        #         "acces_pilotage": accesId,
        #         "addresse": adresse,
        #         "numero_tel": contact,
        #         "langue": "Française",
        #         "theme": "clair",
        #         "fonction": fonction,
        #         "hash_password": password,
        #         "est_bloque": False,
        #     }
        #
        #     databases.create_document(dbAppkey,usersCollection, "unique()", userCreateDoc)
        #
        #     return make_response(jsonify("Utilisateur crée avec succès"), 200)
        #
        # except:
        #     return make_response(jsonify("La requête n'a pas abouti"), 400)

    def getUserIdByEmail(self, email):
        pass

    def getUserDocByEmail(self, email):
        userCollection = dbPerfENERGIE["users"]
        query = userCollection.find({"email":email})
        users = QueryDocToList(query)
        if len(users) == 1 :
            user = users[0]
            del user["_id"]
            del user["token_code"]
            del user["expiration_time"]
            return  user
        return None

    def listUsers(self):
        pass

    def getUserByID(self, id):
        pass

    def resetPassword(self):
        try:

            email = request.get_json()["email"]
            token = request.get_json()["token_code"]
            hashPassword = request.get_json()["password"]

            userCollection = dbPerfENERGIE["users"]
            user = userCollection.find_one({"email": email,"token_code":token})

            if user != None :
                query = {"email": email,"token_code":token}
                newvalues = {"$set": {"password":hashPassword}}
                userCollection.update_one(query, newvalues)
                return make_response({"status": True, "message": "Le mot de passe a été modifié avec succès."}, 200)
            else :
                return make_response({"status": False, "message": "Une erreur est survenue lors du changement du mot passé."}, 400)


        except :
            return make_response({"status": False, "message": "Une erreur est survenue lors du changement du mot passé."}, 400)


    def isUserExistByEmail(self, email):
        pass

    def updatePrefsUser(self):
        pass

    def userToDoc(self, user, hashPwd):
        doc = {
            "email": user["email"],
            "name": user["name"],
            "hashPassword": hashPwd
        }
        return doc
    