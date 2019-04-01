import pandas as pd

def select(df, cols={}):
    """ Select data from dataframe filtering by the columns passed to this
    function and renaming them.

    :param dict cols: The columns which will be selected and their respective
    names.
    :param pandas.DataFrame df: The original dataframe.
    :type file: str or None.
    :return the new DataFrame.
    :rtype pandas.DataFrame.
    """

    selected = df[[k for k in cols]]
    return selected.rename(index=str, columns=cols)
