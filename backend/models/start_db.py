from pathlib import Path

import pandas as pd
from dotenv import dotenv_values
from icecream import colorize, ic
from pymongo import MongoClient

from backend.Database import Database

NAME_DB = "hackaton"


def main():
    ic.configureOutput(
        outputFunction=lambda s: print(colorize(s) + "\n")
    )  # print debug

    db = Database(NAME_DB)
    ic(db)

    path_to_root = Path(__file__) / ".." / ".." / ".."
    path_to_root = path_to_root.resolve()

    path_to_data = path_to_root / "data"

    ic(path_to_data)

    df_poubelles = pd.read_excel(path_to_data / "taux_remplissage_comcom_nebbiu.xlsx")
    ic(df_poubelles)


def get_database(db_name):
    """
    Connects to the MongoDB database specified by the db_name parameter.

    Args:
       db_name (str): The name of the database to connect to.

    Returns:
       pymongo.database.Database: The connected database object.
    """
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

    # Create the database for our example (we will use the same database throughout the tutorial)
    return client[db_name]


if __name__ == "__main__":
    main()
