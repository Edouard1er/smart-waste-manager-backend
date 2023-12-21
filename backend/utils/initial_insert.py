"""insère les données initiales données dans le sujet"""


import pandas as pd
from icecream import colorize, ic
from pathlib import Path

from backend.Database import Database

NAME_DB = "hackaton"


def main():
    ic.configureOutput(
        outputFunction=lambda s: print(colorize(s) + "\n")
    )  # print debug

    db = Database()
    path_to_root = Path(__file__) / ".." / ".." / ".."
    path_to_root= path_to_root.resolve()
    path_to_excel = path_to_root / "data" / "taux_remplissage_comcom_nebbiu.xlsx"

    df = init_excel_to_df(str(path_to_excel))
    
    ic(df)



def init_excel_to_df(path="../../data/taux_remplissage_comcom_nebbiu.xlsx"):
    excel_sheet_names = (pd.ExcelFile(path)).sheet_names
    df_sheets = pd.read_excel(path, sheet_name=excel_sheet_names, header=1)

    list_result = []

    for key, value in df_sheets.items():
        zone = key
        list_gps = []
        for i, row in value.iterrows():
            flagGPS = False
            if i == 0:
                flagGPS = True

            date = row.iloc[1]
            for j in range(2, len(row), 3):
                num_poubelle = int((j - 2) / 3)
                poubelle_nom = str(key) + "-poubelle-" + str(num_poubelle)
                if flagGPS:
                    list_gps.append(row.iloc[j])
                gps = list_gps[num_poubelle]
                remplissage = row.iloc[j + 1]
                coeff_touriste = row.iloc[j + 2]

                list_result.append(
                    [poubelle_nom, zone, coeff_touriste, gps, date, remplissage]
                )

    df_result = pd.DataFrame(
        list_result,
        columns=["nom", "zone", "coeff_touriste", "gps", "date", "remplissage"],
    )
    return df_result

if __name__ == "__main__":
    main()
