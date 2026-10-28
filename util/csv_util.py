# Módulo csv_util.py

"""

Funciones recurrentes para trabajar con ficheros CSV: leer, guardar, eliminar, etc.

"""

import glob
import os
import pandas as pd
import shutil

def read(path, usecols=None, dtype=None, date_formats=None):
    df = pd.read_csv(path, usecols=usecols, dtype=dtype)

    if date_formats is not None:
        for col, date_format in date_formats:
            df[col] = pd.to_datetime(df[col], format=date_format)

    return df

def save(df, path, mode='a', index=False, date_format=None):
    if not os.path.exists(path):
        df.to_csv(path, index=index, date_format=date_format)
    else:
        df.to_csv(path, mode=mode, header=(False if mode == 'a' else True), index=index, date_format=date_format)

def delete(path):
    if os.path.exists(path):
        os.remove(path)

def delete_all(path):
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)

def read_and_merge(folder_path, usecols=None, dtype=None, date_formats=None, path_to_save=None):
    paths = glob.glob(folder_path)
    df = pd.concat([read(path, usecols, dtype, date_formats) for path in paths], ignore_index=True)

    if path_to_save is not None:
        save(df, path_to_save, mode='w')

    return df