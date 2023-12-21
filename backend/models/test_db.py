from backend.Database import Database
from icecream import colorize, ic

NAME_DB = "hackaton"

def main():
    db = Database()
    ic(db)
    

if __name__ == "__main__":
    main()