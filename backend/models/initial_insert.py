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
        for row in value.iterrows():
            print("a")


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
