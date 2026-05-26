import pandas as pd

def load_data():
    titanic = pd.read_csv('data/titanic.csv')
    men = titanic[titanic['Sex'] == 'male']
    return men


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean a pandas DataFrame by removing missing values and normalizing text.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame to clean.

    Returns
    -------
    pd.DataFrame
        A new DataFrame with rows containing missing values dropped and all
        categorical (object/string) column values converted to lowercase.
    """
    df = df.dropna()
    categorical_cols = df.select_dtypes(include=["object", "string"]).columns
    df[categorical_cols] = df[categorical_cols].apply(lambda col: col.str.lower())
    return df