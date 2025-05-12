import pandas as pd
import random

dataset_original = "Datasets/BCSC-risk_factors.csv"
dataset_last_version = 'Last Project/HarmonyForBreastCancer/BCSC_risk_factors_153821.csv'
dataset_process = 'Datasets/BCSC-dataset_153821_0325.csv'

df_process = pd.read_csv(dataset_process)
ids = df_process['year']
df_process.drop('year', axis=1)
for col in df_process.columns:
    print(f"\n--- Conteo de la columna: {col} ---")
    print(df_process[col].value_counts(),'\n')

# 1. Filtrar filas desde la posición 1 hasta la penúltima
df_subset = df_process.iloc[1:-1]  # iloc es indexado por posición

# 2. Contar cuántas veces se repite cada fila (ignorando el índice)
conteo_filas = df_subset.value_counts()

print("Repeticiones de filas:\n", conteo_filas)

