import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

# Directorio para guardar las imágenes
output_dir = Path('../Graficos')
output_dir.mkdir(exist_ok=True)  # Crear la carpeta 'Graficos' si no existe

# Directorio de los datasets
folder_path = Path('../Datasets')

# Cargar el dataset de breast-cancer.data
dataset_name = 'UCI'
file_path = folder_path / 'UCI-breast-cancer.data'

# Definir los nombres de las columnas según la descripción del dataset
column_names = ['Class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat']

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
