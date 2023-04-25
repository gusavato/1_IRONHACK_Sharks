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
import re


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
        info['unique %'] = round(info['unique'] / df.shape[0] * 100, 2)
        cols_info[col] = info
    return pd.DataFrame(cols_info).T


def count_nan_row(df: pd.DataFrame, n_nan=1) -> list:
    """
    Función que recibe un dataframe, y devuelve una lista con el índice de las
    filas que tienen un número de nulos >= n_nan
    """

    nan_index = []

    for fila in df.itertuples():
        count = 0
        for e in fila:
            if e is np.nan:
                count += 1

        if count >= n_nan:
            nan_index.append(fila[0])

    return nan_index

def group_fatal(x):
    """
    Función para formatear correctamente la columna Fatal (Y/N)
    """
    try:    # El bloque try, es por si encuentra un Nan y que no rompa
        if x.strip().upper() == 'N':
            return 'N'
        elif x.strip().upper() == 'Y':
            return 'Y'
        else:
            return x
    except:
        return x
    

def group_sex(x):
    """
    Función para formatear correctamente la columna Sex
    """
    try:    # El bloque try, es por si encuentra un Nan y que no rompa
        if x.strip().upper() == 'M':
            return 'M'
        else:
            return x
    except:
        return x
    
def age_str_to_string(x):
    """
    Función para convertir a entero todos los campos que así lo permitan
    dentro de la columna age
    """
    try:
        int(x)
        return int(x)
    except:
        return x
    
def group_activity(x):
    try:    # El bloque try, es por si encuentra un Nan y que no rompa
        if 'surf' in x.lower():
            return 'Surfing'
        elif 'diving' in x.lower():
            return 'Diving'
        elif 'fish' in x.lower():
            return 'Fishing'
        elif 'swim' in x.lower():
            return 'Swimming'
        elif 'board' in x.lower():
            return 'Boarding'
        else:
            return x
    except:
        return x    
    
def group_time(x):
    """
    Función que se encarga de examinar la cadena de texto recogida en Time.
    Si el patrón de número + h + número se detecta, compara valores para 
    asignar un momento del día
    """
    patron = r'\dh\d'
    try:    # El bloque try, es por si encuentra un Nan y que no rompa
        if re.findall(patron,x):
            if 9 < int(x[:2]) <= 14:
                return 'Morning'
            elif 14 < int(x[:2]) <= 21:
                return 'Afternoon'
            elif (21 < int(x[:2]) <= 23) or (0 <= int(x[:2]) <= 9):
                return 'Night'
            else:
                return x
    except:
        return x   
    
def check_ques(x):
    """
    Función que chequea las instancias de Species, que nos indican que los 
    ataque son cuestionados
    """
    try:
        if 'quest' in x.lower():
            return True
        else:
            return False
    except:
        return False
