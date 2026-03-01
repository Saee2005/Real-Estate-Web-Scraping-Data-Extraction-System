import pandas as pd

def clean_data(data):
    df = pd.DataFrame(data)

    df.drop_duplicates(inplace=True)
    df.fillna("N/A", inplace=True)

    # Clean price column (remove $)
    if "Price" in df.columns:
        df["Price"] = df["Price"].str.replace("$", "", regex=False)

    return df