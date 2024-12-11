"""
data utilities for CSC-323
"""
import random
import pandas as pd


def make_df_from_results(results: list) -> pd.DataFrame:
    """
    given a list of list of results, return a dataframe
    where every list 
    """

    #generate column names
    col_names = [f"col_{i}" for i in range(30)]

    #convert every list to a series
    all_series = [pd.Series(l) for l in results]

    #make empty df with column names
    df = pd.DataFrame(columns=col_names)

    #make every series its own colum
    for c, s in zip(col_names, all_series):
        df[c] = s
    return df


def make_quartiles(df: pd.DataFrame) -> tuple:
    """
    given a dataframe, return following per-row statistics:

    npmeans:np.array the mean of values in each row
    npq25:np.array the 25th percentile
    npq75:np.array the 75th percentile

    """
    means = df.mean(axis=1)
    q25 = df.quantile(0.25, axis=1)
    q75 = df.quantile(0.75, axis=1)
    npmeans = means.to_numpy()
    npq25 = q25.to_numpy()
    npq75 = q75.to_numpy()
    return npmeans, npq25, npq75

def probability(p: float):
    """
    return True with probability p
    """
    return random.random() <= p