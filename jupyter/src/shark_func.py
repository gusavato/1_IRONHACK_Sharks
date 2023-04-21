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

    if method == 'sum':
        nan_cols = df.isna().sum()
    elif method == 'avg':
        nan_cols = df.isna().mean()
    if disp == True:
        display(nan_cols[nan_cols > 0])

    return nan_cols
