from pymongo import MongoClient
from dotenv import dotenv_values
from icecream import ic, colorize


def main():
    ic.configureOutput(outputFunction=lambda s: print(colorize(s) + "\n")) # print debug
    config = dotenv_values(".env")
    ic(config)
    


def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "aa"
   
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['user_shopping_list']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   main()