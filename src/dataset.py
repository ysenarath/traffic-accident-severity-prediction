import pandas as pd


def load_dataset():
    df = pd.read_csv('../data/US_Accidents_Dec19.csv')
    return df
