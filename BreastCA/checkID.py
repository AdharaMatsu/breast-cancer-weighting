
import pandas as pd
import numpy as np
import time

#from fontTools.ttx import process

def equal_file(filename):
    dataset_generated = pd.read_csv(filename)

    # Verificar que las filas en las posiciones 0 a 9 son iguales
    for i in range(min(len(df_processed), len(dataset_generated))):  # Asegura que no se pase del tamaño de los DataFrames
        fila1 = df_processed.iloc[i, :10].values # Seleccionar las primeras 10 columnas de la fila
        fila2 = dataset_generated.iloc[i, :10].values

        if not (fila1 == fila2).all(): # Comparar las filas (sin importar otras columnas)
            print(f"No todas las filas son iguales, en la posición {i} .")
            break
    else:
        print("Todas las filas son iguales.")

def check_duplicates(attribute): # ID Repetidos - Descartado
    repetidos = df_processed[attribute].value_counts()
    repetidos = repetidos[repetidos > 1]  # Filtrar los que aparecen más de una vez

    return repetidos

def check_for_ID():
    processed_header = df_processed.columns.tolist()
    original_header = df_original.columns.tolist()
    it = 0

    new_column_name = original_header[-2]
    processed_header = processed_header[:-1] + [new_column_name] + [processed_header[-1]]
    new_data = []

    while it < len(df_processed):
        process_list = df_processed.iloc[it].values
        ID = process_list[0]
        edit_process_list = process_list[1:-1]
        original_list = df_original.iloc[ID - 1, 1:-2].values
        status = np.array_equal(edit_process_list, original_list)
        if not status:
            print(False)
        new_attribute = df_original.iloc[ID - 1].values
        process_list = np.insert(process_list, -2, new_attribute[-2])
        new_data.append(process_list)

        it = it + 1
    df_nuevo = pd.DataFrame(new_data, columns=original_header)
    df_nuevo.to_csv('Datasets/BCSC-dataset_153821_0325.csv', index=False)

start_time = time.time()

dataset_original = "Datasets/BCSC LPNP-risk_factors_summarized-LPNP.csv"
dataset_process = 'Last Project/HarmonyForBreastCancer/BCSC_risk_factors_153821.csv'

df_processed = pd.read_csv(dataset_process)
df_original = pd.read_csv(dataset_original)


def check_counter(df, dfB, df_process): # checar ID numero de veces que se repite
    lista = []
    for i in range(len(df_process)):
        A_np = df.iloc[i,1:-1].values
        B_np = dfB.iloc[:, 1:-2].values

        conteo = np.sum(np.all(B_np == A_np, axis=1))
        if len(lista) == 0:
            lista.append(conteo)
        elif not conteo in lista:
            lista.append(conteo)


# check_duplicates(processed_header[0])
# check_counter()
check_for_ID() # revisar por ID si es semejante
equal_file('Datasets/BCSC-dataset_153821_0325.csv')

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos")

