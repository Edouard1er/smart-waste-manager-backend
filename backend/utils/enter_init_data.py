from pathlib import Path

import pandas as pd
from icecream import colorize, ic

from backend.Database import Database

ZONE_TO_POP = {
        "Olmeta di tuda": 442,
        "Rapale": 149,
        "Santu petro di tenda": 360,
        "Barbaggio": 266,
        "Sorio": 137,
        "Pieve": 118,
        "Oletta": 1_587,
        "Saint florent": 1_634,
        "Poggio oletta": 218,
        "Vallecalle": 131,
        "Rutali": 387,
        "Farinole": 197,
        "Murato": 625,
        "Patrimonio": 746,
        "Casta": 50,
        "San gavino di tenda": 68,
    }


def main():
    ic.configureOutput(
        outputFunction=lambda s: print(colorize(s) + "\n")
    )  # print debug

    

    path_to_root = Path(__file__) / ".." / ".." / ".."
    path_to_root = path_to_root.resolve()
    path_to_data = path_to_root / "data"
    ic(path_to_data)
    db = Database()
    insert_data(db, path_to_data / "taux_remplissage_comcom_nebbiu.xlsx")


def insert_data(db, path):
    excel_sheet_names = (pd.ExcelFile(path)).sheet_names
    df_sheets = pd.read_excel(path, sheet_name=excel_sheet_names, header=1)

    for key, value in df_sheets.items():
        zone = key.strip().capitalize()
        list_gps = []
        for i, row in value.iterrows():
            date = row.iloc[1]

            for j in range(2, len(row), 3):
                if i == 0:
                    num_habitant= ZONE_TO_POP[zone]
                    gps = row.iloc[j]
                    poubelle_nom = str(key) + "-poubelle-" + str(num_poubelle)
                    coeff_touriste = row.iloc[j + 2]
                    (j - 2) / 3)
                    
                    ic(zone, num_habitant, gps, poubelle_nom, coeff_touriste)

                remplissage = row.iloc[j + 1]


if __name__ == "__main__":
    main()
