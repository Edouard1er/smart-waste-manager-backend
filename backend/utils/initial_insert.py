"""insère les données initiales données dans le sujet"""

from pathlib import Path

import pandas as pd
from icecream import colorize, ic

from backend.Database import Database

NAME_DB = "hackaton"


def main():
    ic.configureOutput(
        outputFunction=lambda s: print(colorize(s) + "\n")
    )  # print debug

    db = Database()

    # df = pd.DataFrame()
    # ic()

    # print(df)
    excel_sheet_names, df = get_initial_data()

    for key, value in df.items():
        name_zone = excel_sheet_names[key]
        # key_zone = Database.add_data_zone(nom=name_zone)

        # key_poubelle = Database.add_data_poubelle

        for row in value.iloc[:, 2:].iterrows():
            row = row[1]

            for i in range(0, len(row), 3):
                coeff_touriste = row[i + 2]
                remplissage = row[i + 1]
                ic(coeff_touriste)
                ic(remplissage)

            # db.add_data_poubelle(id_zone=key_zone)
            # db.add_data_historique_poubelle


def get_initial_data():
    path_to_root = Path(__file__) / ".." / ".." / ".."
    path_to_root = path_to_root.resolve()

    path_to_data = path_to_root / "data"

    excel_sheet_names = (
        pd.ExcelFile(path_to_data / "taux_remplissage_comcom_nebbiu.xlsx")
    ).sheet_names
    df = pd.read_excel(
        path_to_data / "taux_remplissage_comcom_nebbiu.xlsx", sheet_name=list(range(16))
    )

    return excel_sheet_names, df


if __name__ == "__main__":
    main()
