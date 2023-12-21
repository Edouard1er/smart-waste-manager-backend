from pathlib import Path

import pandas as pd
from dotenv import dotenv_values
from icecream import colorize, ic
from pymongo import MongoClient

from datetime import datetime

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
    
    
    def add_data_poubelle(self, coef_tourist, densite, zone, next_collection_date):
        collection = self.client.poubelle
        
        # Création du document
        document = {
            "coef_touristes": coef_tourist,
            "densite": densite,
            "zone": zone,
            "nextCollectionDate": datetime.strptime(next_collection_date, "%Y-%m-%d")
        }

        # Insertion du document dans la collection
        key = collection.insert_one(document)
        return key
