"""
Módulo donde recogere todas las funciones necesarias para la limpieza
del dataframe attacks.csv ubicado en la carpeta data

+   check_nan_cols: recibe un dataframe y retorna un Serie, con el número de 
    nulos por cada columna del dataframe (method = sum), o el porcentaje 
    (method = 'avg').
    Si se asigna a una variable, muestra el resultado con las columnas que
    tengan nulos, a menos que se indique lo contrario (display = False)

"""
import pandas as pd
import numpy as np


def check_nan_cols(df: pd.DataFrame(),
                   method='sum',
                   disp=True) -> pd.Series():
    """
    check_nan_cols: recibe un dataframe y retorna un Serie, con el número de 
    nulos por cada columna del dataframe (method = sum), o el porcentaje 
    (method = 'avg').
    Si se asigna a una variable, muestra el resultado con las columnas que
    tengan nulos, a menos que se indique lo contrario (display = False)

    """

    if method == 'sum':
        nan_cols = df.isna().sum()
    elif method == 'avg':
        nan_cols = round(df.isna().mean()*100, 2)
    if disp == True:
        display(nan_cols[nan_cols > 0])

    return nan_cols


def cols_info(df: pd.DataFrame) -> int:
    """
    Devulve información detallada de cada columna
    """
    cols_info = dict()
    for col in df:
        info = dict()
        info['Col Type'] = df[col].dtype
        info['Nulos'] = int(check_nan_cols(df[col], disp=False))
        info['str'] = df[col][df[col].apply(lambda x: type(x) == str)].shape[0]
        info['float'] = df[col][df[col].apply(
            lambda x: type(x) == float)].shape[0]
        info['int'] = df[col][df[col].apply(lambda x: type(x) == int)].shape[0]
        info['bool'] = df[col][df[col].apply(
            lambda x: type(x) == bool)].shape[0]
        info['date'] = df[col][df[col].apply(
            lambda x: type(x) == np.datetime64)].shape[0]
        info['float==nan'] = info['Nulos'] == info['float']
        info['unique'] = df[col].unique().size
        cols_info[col] = info
    return pd.DataFrame(cols_info).T
