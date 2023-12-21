from dotenv import dotenv_values
from icecream import colorize, ic
from pymongo import MongoClient

NAME_DB = "hackaton"


def main():
    ic.configureOutput(
        outputFunction=lambda s: print(colorize(s) + "\n")
    )  # print debug

    db = get_database(NAME_DB)


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
        print("connexion to db established !")
    except ConnectionError:
        print("Server not available")

    # Create the database for our example (we will use the same database throughout the tutorial)
    return client[db_name]


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    main()
