import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

# Directorio para guardar las imágenes
output_dir = Path('../Graficos')
output_dir.mkdir(exist_ok=True)  # Crear la carpeta 'Graficos' si no existe

# Directorio de los datasets
folder_path = Path('../Datasets')

# Cargar el dataset de wdbc.data
dataset_name = 'Wisconsin'
file_path = folder_path / 'Wisconsin-data.csv'

# Definir los nombres de las columnas según la descripción del dataset
column_names = ['ID', 'Diagnosis'] + [f'feature_{i}' for i in range(1, 31)]

# Cargar el dataset
df = pd.read_csv(file_path, names=column_names)

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

# Seleccionamos algunas columnas numéricas para el análisis de boxplot
columns_to_plot = ['feature_1', 'feature_2', 'feature_3']  # Ejemplo

# Crear histogramas y diagramas de caja para las columnas seleccionadas y guardarlos en archivos
for column in columns_to_plot:
    hist_path = output_dir / f'{dataset_name}_histograma_{column}.png'
    boxplot_path = output_dir / f'{dataset_name}_boxplot_{column}.png'

    # Histograma
    df[column].hist()
    plt.savefig(hist_path)  # Guardar el gráfico en lugar de mostrarlo
    #plt.clf()  # Limpiar la figura para el siguiente gráfico

    # Diagrama de caja para detectar valores atípicos
    sns.boxplot(x=df[column])
    plt.savefig(boxplot_path)  # Guardar el gráfico en lugar de mostrarlo
    #plt.clf()  # Limpiar la figura para el siguiente gráfico

print(f"Gráficos guardados\n\n")
