import pandas as pd


# This function transform the data to into a pandas dataframe
def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    # Rename all the columns in the dataframe and converts them to lowercase  
    df = df.rename(columns=str.lower)

    # Assigns the current timestamp to a new column
    df["extracted_date"] = pd.Timestamp.now()

    return df