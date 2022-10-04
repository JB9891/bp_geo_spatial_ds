import pandas as pd


def read_prep_data():
    # Read data
    df_import = pd.read_csv("data/melbourne/Melbourne_housing_FULL.csv")
    df_import.columns = df_import.columns.str.strip().str.replace(" ", "_").str.lower()
    df_import["date"] = pd.to_datetime(df_import["date"])

    # Drop location columns and simply df
    drops = [
        "address",
        "postcode",
        "councilarea",
        "bedroom2",
        "suburb",
        "regionname",
        "propertycount",
        "type",
        "method",
        "sellerg",
        "date",
    ]

    df_housing = df_import.drop(columns=drops)

    # drop year build outlier
    df_housing = df_housing[df_housing["yearbuilt"] != df_housing["yearbuilt"].min()]

    # Drop nan values
    df_housing = df_housing.dropna().reset_index(drop=True)

    return df_housing
