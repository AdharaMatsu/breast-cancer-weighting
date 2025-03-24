import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

output_dir = Path('../Graficos')  # Directorio para guardar las imágenes
output_dir.mkdir(exist_ok=True)  # Crear la carpeta 'Graficos' si no existe

folder_path = Path('../Datasets')
filenames = []
names = [file.name for file in folder_path.iterdir() if
         file.is_file() and (file.suffix == '.csv' or file.suffix == '.data')]

for e in names:  # Crear una lista de tuplas con nombres y nombres de archivos
    temp1 = e.split('-')
    temp = (temp1[0], e)
    filenames.append(temp)
# 0 -> BCSC-risk_factors.csv
# 3 -> BCSC LPP-risk_factors-LPP.csv
file = 3
dataset_name = filenames[file][0]  # Nombre del dataset
print('DATASET: ', dataset_name, '\n', filenames[file][1], '\n')

df = pd.read_csv(str(folder_path) + '/' + filenames[file][1])

# Ver el número de filas, columnas y tipos de datos
print(df.info())

# Resumen estadístico para todas las columnas numéricas
print(df.describe())

# Resumen estadístico de todas las columnas, incluyendo las categóricas
print(df.describe(include='all'))

# Obtener el nombre de la última columna
last_column = df.columns[-1]
print(f"El nombre de la última columna es: {last_column}")

# Ver los valores únicos y su frecuencia para la última columna
print(df[last_column].value_counts())

# Contar los valores nulos por columna
print(df.isnull().sum())

# Si la última columna es numérica, continuar con el análisis
if pd.api.types.is_numeric_dtype(df[last_column]):
    q1 = df[last_column].quantile(0.25)
    q3 = df[last_column].quantile(0.75)
    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    outliers = df[(df[last_column] < limite_inferior) | (df[last_column] > limite_superior)]
    print(outliers)

    # Crear histogramas y diagramas de caja para la última columna y guardarlos en archivos
    hist_path = output_dir / f'{dataset_name}_histograma_{last_column}.png'
    boxplot_path = output_dir / f'{dataset_name}_boxplot_{last_column}.png'

    # Histograma
    df[last_column].hist()
    plt.savefig(hist_path)  # Guardar el gráfico en lugar de mostrarlo
    plt.clf()  # Limpiar la figura para el siguiente gráfico

    # Diagrama de caja para detectar valores atípicos
    sns.boxplot(x=df[last_column])
    plt.savefig(boxplot_path)  # Guardar el gráfico en lugar de mostrarlo
    plt.clf()  # Limpiar la figura para el siguiente gráfico

print(f"Gráficos guardados\n\n")
