from files import dataset_original, dataset_process

import pandas as pd

df = pd.read_csv(dataset_process)
#num_filas = df.shape[0]  # numero de filas
#print(f"El CSV tiene {num_filas} filas.")
#print(df.iloc[0].to_numpy()) # datos por fila

#for column in df.columns[1:]:
#       repetead_values = df[column].value_counts()
#        print(f"\nValores repetidos en '{column}':")
#        print(repetead_values)
valores_unicos = df['age_group_5_years'].unique()
print(valores_unicos)
#        repetead_values = repetead_values[repetead_values > 1]  # Filtrar solo valores repetidos

        #if not repetead_values.empty:
        #    print(f"\nValores repetidos en '{column}':")
        #    print(repetead_values)
