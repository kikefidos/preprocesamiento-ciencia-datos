import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def cargar_datos(ruta):
    """Carga un dataset CSV en un DataFrame de pandas"""
    return pd.read_csv(ruta)

def limpiar_datos(df):
    """Elimina duplicados y valores nulos"""
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def escalar_datos(df, columnas):
    """Aplica escalado Min-Max a las columnas seleccionadas"""
    scaler = MinMaxScaler()
    df[columnas] = scaler.fit_transform(df[columnas])
    return df

def preprocesar_dataset(ruta):
    """Ejecuta el flujo completo de preprocesamiento"""
    df = cargar_datos(ruta)
    df = limpiar_datos(df)
    df = escalar_datos(df, df.select_dtypes(include='number').columns)
    return df