# Primera version de EDA

from preprocessing.filenamesList import filenames
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# for file in range(1):   
file = 0
print('Dataset', filenames[file][0], ': \n', filenames[file][1], '\n')
df = pd.read_csv('Datasets/' + filenames[file][1])

# Ver el número de filas, columnas y tipos de datos
print(df.info())

# Resumen estadístico para todas las columnas numéricas
print(df.describe())

# Verificar valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Proporción de valores nulos
print("\nProporción de valores nulos por columna:")
print(df.isnull().mean())

# 5. Gráfica de valores nulos (si los hay)
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis', cbar_kws={'label': 'Missing Values'})
plt.title('Valores Nulos en el Dataset')
plt.show()

# 6. Distribución de variables numéricas con histogramas
df_numeric = df.select_dtypes(include='number')
df_numeric.hist(bins=30, figsize=(15, 15))
plt.suptitle('Distribución de Variables Numéricas', fontsize=16)
plt.show()
# Visualización de datos
# CreateCharts.Charts(df, filenames[file][0])

# 8. Detección de valores atípicos con gráficos de cajas y bigotes
plt.figure(figsize=(15, 6))
df_numeric.plot(kind='box', subplots=True, layout=(1, len(df_numeric.columns)), sharex=False, sharey=False)
plt.suptitle('Detección de Valores Atípicos (Boxplot)', fontsize=16)
plt.show()

# 9. Correlación entre variables numéricas
plt.figure(figsize=(12, 8))
corr_matrix = df_numeric.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title('Matriz de Correlación')
plt.show()

# 10. Análisis de variables categóricas
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nFrecuencia de la variable categórica '{col}':")
    print(df[col].value_counts())

    # Gráfica de barras para cada variable categórica
    plt.figure(figsize=(10, 6))
    sns.countplot(x=col, data=df)
    plt.title(f'Frecuencia de la variable categórica: {col}')
    plt.show()

# 11. Gráfico de dispersión para relaciones entre variables numéricas
sns.pairplot(df_numeric)
plt.suptitle('Gráficas de Dispersión entre Variables Numéricas', fontsize=16)
plt.show()

print("\n")  # Línea en blanco para separar cada dataset
