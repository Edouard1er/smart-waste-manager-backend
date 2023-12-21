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

    zone_nom_to_id = {}
    for key, value in df_sheets.items():
        zone = key.strip().capitalize()

        num_habitant = ZONE_TO_POP[zone]
        zone_nom_to_id[zone] = db.add_data_zone(
            nom=zone, gps=None, densite=num_habitant, nb_poubelles=None
        )

        for i, row in value.iloc[:, :6].iterrows():
            date = row.iloc[1]  # noqa: F841
            list_ids_poubelles = []
            for j in range(2, len(row), 3):
                num_poubelle = int((j - 2) / 3)
                coeff_touriste = row.iloc[j + 2]

                if i == 0:
                    gps = row.iloc[j]
                    poubelle_nom = str(key) + "-poubelle-" + str(num_poubelle)
                    print("insert :")
                    ic(
                        zone_nom_to_id[zone].inserted_id,
                        num_habitant,
                        gps,
                        num_poubelle,
                        poubelle_nom,
                        coeff_touriste,
                    )

                    list_ids_poubelles.append(
                        db.add_data_poubelle(
                            id_zone=zone_nom_to_id[zone].inserted_id,
                            gps=gps,
                            densite=None,
                            coef_tourist=None,
                            next_collection_date=None,
                        )
                    )

                remplissage = row.iloc[j + 1]  # noqa: F841

                db.add_data_historiquePoubelle(
                    id_poubelle=list_ids_poubelles[num_poubelle],
                    niveau_remplissage=remplissage,
                    coef_tourist=coeff_touriste,
                    date=date,
                )
                # db.add_data_historique(list_ids_poubelles[num_poubelle], coeff_touriste, date, remplissage)


if __name__ == "__main__":
    main()
