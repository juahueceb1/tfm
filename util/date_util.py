# Módulo date_util.py

"""

Funciones recurrentes para trabajar con fechas: rangos, contar días, etc.

"""

import numpy as np
import pandas as pd

def create_range(start_date, end_date, date_format=None, freq='D'):
    return pd.DataFrame({'date': pd.date_range(pd.to_datetime(start_date, format=date_format), pd.to_datetime(end_date, format=date_format), freq=freq)})

def create_ranges(df, start_date_col, end_date_col, freq='D'):
    # Crea listas que contienen todas las fechas de cada intervalo. A continuación, une los valores de todas las listas.
    dates = (df.apply(lambda row: pd.date_range(row[start_date_col], row[end_date_col], freq=freq), axis=1)
               .explode()
               .reset_index(drop=True))

    return pd.DataFrame({'date': dates})

def count_days(date_1, date_2, date_format=None):
    return (pd.to_datetime(date_2, format=date_format) - pd.to_datetime(date_1, format=date_format)).days + 1

def add_cyclic_coding(df):
    # Obtener ordinal del día de la semana y año.
    day_of_week = df['date'].dt.dayofweek + 1 # Se suma 1 porque el lunes se identifica con el 0.
    day_of_year = df['date'].dt.dayofyear

    # Determinar los días totales del año en función de si es bisiesto o no.
    days_in_year = np.where(df['date'].dt.is_leap_year, 366.0, 365.0)

    # Añadir codificación cíclica para días de la semana y año.
    df['sin_day_of_week'] = np.sin(2 * np.pi * day_of_week / 7.)
    df['cos_day_of_week'] = np.cos(2 * np.pi * day_of_week / 7.)
    df['sin_day_of_year'] = np.sin(2 * np.pi * day_of_year / days_in_year)
    df['cos_day_of_year'] = np.cos(2 * np.pi * day_of_year / days_in_year)

    return df