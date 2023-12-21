from pathlib import Path

import pandas as pd
from icecream import colorize, ic


def main():
    ic.configureOutput(
        outputFunction=lambda s: print(colorize(s) + "\n")
    )  # print debug

    zone_to_pop = {
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

    path_to_root = Path(__file__) / ".." / ".." / ".."
    path_to_root = path_to_root.resolve()
    path_to_data = path_to_root / "data"
    ic(path_to_data)
    insert_data(path_to_data / "taux_remplissage_comcom_nebbiu.xlsx")


def insert_data(path="../../data/taux_remplissage_comcom_nebbiu.xlsx"):
    excel_sheet_names = (pd.ExcelFile(path)).sheet_names
    df_sheets = pd.read_excel(path, sheet_name=excel_sheet_names, header=1)

    list_result = []

    for key, value in df_sheets.items():
        zone = key.strip().capitalize()
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
