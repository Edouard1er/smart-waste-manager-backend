from datetime import datetime
from dotenv import dotenv_values
from icecream import ic
from pymongo import MongoClient


class Database:
    def __init__(self, db_name="hackaton"):
        config = dotenv_values(".env")

        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        CONNEXION_STRING = config["CONNEXION_STRING"]
        ic(CONNEXION_STRING)

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        client = MongoClient(CONNEXION_STRING)

        try:
            client.admin.command("ismaster")
            print("connexion to db established !\n")
        except ConnectionError:
            print("Server not available\n")

        self.client = client

    def add_data_poubelle(self, id_zone, coef_tourist, densite, next_collection_date):
        collection = self.client.poubelle

        # Création du document
        document = {
            "coef_touristes": coef_tourist,
            "densite": densite,
            "id_zone": id_zone,
            "nextCollectionDate": datetime.strptime(next_collection_date, "%Y-%m-%d"),
        }

        # Insertion du document dans la collection
        key = collection.insert_one(document)
        return key
    
    def add_data_collecteur(self, id_zone, matricule, nom,prenom, username, password, role):
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
        collection = self.client.historique
        
        # Création du document
        document = {
            "id_poubelle": id_poubelle,
            "coef_touristes": coef_tourist,
            "date": date,
            "niveau_remplissage": niveau_remplissage
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
            "niveau_remplissage": niveau_remplissage
        }

        # Insertion du document dans la collection
        key = collection.insert_one(document)
        return key

    def get_data_poubelle(self):
        collection = self.client.poubelle
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
        document = {
            "gps": gps,
            "densite": densite,
            "nb_poubelles": nb_poubelles
        }

        # Insertion du document dans la collection
        key = collection.update_one({"_id": id}, {"$set": document})
        return key
    def update_data_collecteur(self, id, matricule, nom,prenom, username, password, role):
        collection = self.client.collecteur

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
        key = collection.update_one({"_id": id}, {"$set": document})
        return key

    def delete_data_poubelle(self, id):
        collection = self.client.poubelle
        return collection.delete_one({"_id": id})

    def delete_data_zone(self, id):
        collection = self.client.zone
        return collection.delete_one({"_id": id})

    def delete_data_collecteur(self, id):
        collection = self.client.collecteur
        return collection.delete_one({"_id": id})
    
    def get_data_poubelle_by_zone(self, id_zone):
        collection = self.client.poubelle
        return collection.find({"id_zone": id_zone})

    def get_data_collecteur_by_zone(self, id_zone):
        collection = self.client.collecteur
        return collection.find({"id_zone": id_zone})
