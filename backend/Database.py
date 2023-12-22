import os
from datetime import datetime
from bson import ObjectId

from dotenv import load_dotenv
from icecream import ic  # noqa: F401
from pymongo import MongoClient

load_dotenv()


class Database:
    def __init__(self, db_name="hackaton"):
        CONNEXION_STRING = "mongodb+srv://silvanshine:g5Kgw38pHWJEDMlO@cluster-hackaton-sitec.yhj9j2s.mongodb.net/"

        client = MongoClient(CONNEXION_STRING)
        mongo = client["hackaton"]

        try:
            client.admin.command("ismaster")
            print("connexion to db established !\n")
        except ConnectionError:
            print("Server not available\n")

        self.client = mongo

    def add_data_poubelle(
        self, id_zone, coef_tourist, densite, next_collection_date, gps
    ):
        collection = self.client.poubelle

        if next_collection_date:
            next_collection_date = datetime.strptime(next_collection_date, "%Y-%m-%d")

        # Création du document
        document = {
            "coef_touristes": coef_tourist,
            "densite": densite,
            "id_zone": id_zone,
            "gps": gps,
            "nextCollectionDate": next_collection_date,
        }

        # Insertion du document dans la collection
        key = collection.insert_one(document)
        return key

    def add_data_collecteur(
        self, id_zone, matricule, nom, prenom, username, password, role
    ):
        collection = self.client.collecteur

        # Création du document
        document = {
            "id_zone": id_zone,
            "matricule": matricule,
            "nom": nom,
            "prenom": prenom,
            "username": username,
            "password": password,
            "role": role,
        }

        # Insertion du document dans la collection
        key = collection.insert_one(document)
        return key

    def add_data_zone(self, nom, gps, densite, nb_poubelles):
        collection = self.client.zone

        # Création du document
        document = {
            "nom": nom,
            "gps": gps,
            "densite": densite,
            "nb_poubelles": nb_poubelles,
        }

        # Insertion du document dans la collection
        key = collection.insert_one(document)
        return key

    def add_data_historique(self, id_poubelle, coef_tourist, date, niveau_remplissage):
        collection = self.client.historiquePoubelle

        # Création du document
        document = {
            "id_poubelle": id_poubelle,
            "coef_touristes": coef_tourist,
            "date": date,
            "niveau_remplissage": niveau_remplissage,
        }

        # Insertion du document dans la collection
        key = collection.insert_one(document)
        return key

    def add_data_trajet(self, id_collecteur, id_poubelle, date, niveau_remplissage):
        collection = self.client.trajet

        # Création du document
        document = {
            "id_collecteur": id_collecteur,
            "id_poubelle": id_poubelle,
            "date": date,
            "niveau_remplissage": niveau_remplissage,
        }

        # Insertion du document dans la collection
        key = collection.insert_one(document)
        return key

    def get_data_poubelle(self):
        collection = self.client.poubelle
        print("eddy",list(collection.find()))
        return collection.find()

    def get_data_zone(self):
        collection = self.client.zone
        return collection.find()

    def get_data_collecteur(self):
        collection = self.client.collecteur
        return collection.find()

    def get_data_poubelle_by_id(self, id):
        collection = self.client.poubelle
        return collection.find_one({"_id": id})

    def get_data_zone_by_id(self, id):
        collection = self.client.zone
        return collection.find_one({"_id": id})

    def get_data_collecteur_by_id(self, id):
        collection = self.client.collecteur
        return collection.find_one({"_id": id})

    def update_data_poubelle(self, id, coef_tourist, densite, next_collection_date):
        collection = self.client.poubelle

        # Création du document
        document = {
            "coef_touristes": coef_tourist,
            "densite": densite,
            "nextCollectionDate": datetime.strptime(next_collection_date, "%Y-%m-%d"),
        }

        # Insertion du document dans la collection
        key = collection.update_one({"_id": id}, {"$set": document})
        return key

    def update_data_zone(self, id, gps, densite, nb_poubelles):
        collection = self.client.zone

        # Création du document
        document = {"gps": gps, "densite": densite, "nb_poubelles": nb_poubelles}

        # Insertion du document dans la collection
        key = collection.update_one({"_id": id}, {"$set": document})
        return key

    def update_data_collecteur(
        self, id, matricule, nom, prenom, username, password, role
    ):
        collection = self.client.collecteur
        
        _id = ObjectId(id)

        # Création du document
        document = {
            "matricule": matricule,
            "nom": nom,
            "prenom": prenom,
            "username": username,
            "password": password,
            "role": role,
        }

        # Insertion du document dans la collection
        key = collection.update_one({"_id": _id}, {"$set": document})
        return key

    def delete_data_poubelle(self, id):
        collection = self.client.poubelle
        return collection.delete_one({"_id": id})

    def delete_data_zone(self, id):
        collection = self.client.zone
        return collection.delete_one({"_id": id})

    def delete_data_collecteur(self, id):
        collection = self.client.collecteur
        _id = ObjectId(id)
        return collection.delete_one({"_id": _id})

    def get_data_poubelle_by_zone(self, id_zone):
        collection = self.client.poubelle
        return collection.find({"id_zone": id_zone})

    def get_data_collecteur_by_zone(self, id_zone):
        collection = self.client.collecteur
        return collection.find({"id_zone": id_zone})
    
    def get_data_poubelle_by_date_historique_and_zone(self, id_zone, date_historique):
        collection_poubelle = self.client.poubelle
        collection_historique = self.client.historiquePoubelle

        date_historique = datetime.strptime(date_historique, "%Y-%m-%d")
        id_zone = ObjectId(id_zone)
        
        # Agrégation entre les collections
        
        # result = collection_poubelle.find_one({"id_zone": id_zone})
        result = collection_poubelle.aggregate([
            {
                "$match": {
                    "id_zone": id_zone
                }
            },
            {
                "$lookup": {
                    "from": "historiquePoubelle",
                    "localField": "_id",
                    "foreignField": "id_poubelle",
                    "as": "historique"
                }
            },
            {
                "$unwind": {
                    "path": "$historique",
                    "preserveNullAndEmptyArrays": True
                }
            },
            {
                "$match": {
                    "historique.date": date_historique
                }
            },
            {
                "$project": {
                    "_id": 1,
                    "coef_touristes": 1,
                    "densite": 1,
                    "id_zone": 1,
                    "gps": 1,
                    "nextCollectionDate": 1,
                    "historique.coef_touristes": 1,
                    "historique.date": 1,
                    "historique.niveau_remplissage": 1
                }
            }
        ])
        

        return list(result)
