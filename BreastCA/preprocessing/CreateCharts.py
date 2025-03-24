from pathlib import Path
import os
import matplotlib.pyplot as plt
import seaborn as sns
import math

output_route = Path('../Charts')  # Directorio para guardar las imágenes
os.makedirs(output_route, exist_ok=True)  # Crear la carpeta si no existe

def Charts(df, dataset_name):
    """
    Genera y guarda varias gráficas para un DataFrame.

    Args:
        df (pd.DataFrame): El DataFrame con los datos.
        dataset_name (str): El nombre del dataset para usar en los archivos generados.
    """
    # Filtrar solo las columnas numéricas
    df_numeric = df.select_dtypes(include='number')

    # Histograma
    plt.figure(figsize=(20, 20))
    df_numeric.hist(bins=30, figsize=(20, 20))  # Histograma más grande
    hist_path = os.path.join(output_route, f"{dataset_name}_hist.png")
    plt.savefig(hist_path, dpi=300, bbox_inches='tight')
    print(f"Histograma guardado en: {hist_path}")
    plt.close()

    # Gráfica de densidad
    num_cols = len(df_numeric.columns)  # Número de columnas numéricas
    rows = math.ceil(math.sqrt(num_cols))  # Número de filas para un layout cuadrado
    cols = math.ceil(num_cols / rows)  # Número de columnas necesario

    plt.figure(figsize=(7 * cols, 7 * rows))
    df_numeric.plot(kind='density', subplots=True, layout=(rows, cols), sharex=False)
    density_path = os.path.join(output_route, f"{dataset_name}_density.png")
    plt.savefig(density_path, dpi=300, bbox_inches='tight')
    print(f"Gráfico de densidad guardado en: {density_path}")
    plt.close()

    # Gráfica de cajas y bigotes
    plt.figure(figsize=(7 * cols, 7 * rows))  # Ajustar el tamaño de la figura
    df_numeric.plot(kind='box', subplots=True, layout=(rows, cols), sharex=False, sharey=False)
    boxplot_path = os.path.join(output_route, f"{dataset_name}_boxplot.png")
    plt.savefig(boxplot_path, dpi=300, bbox_inches='tight')
    print(f"Gráfico de cajas y bigotes guardado en: {boxplot_path}")
    plt.close()

    # Matriz de correlación
    plt.figure(figsize=(15, 10))  # Tamaño ajustado para la matriz de correlación
    sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
    corr_path = os.path.join(output_route, f"{dataset_name}_correlation.png")
    plt.savefig(corr_path, dpi=300, bbox_inches='tight')
    print(f"Matriz de correlación guardada en: {corr_path}")
    plt.close()

    # Gráficas de dispersión (pairplot) para columnas numéricas
    pairplot_path = os.path.join(output_route, f"{dataset_name}_pairplot.png")
    sns.pairplot(df_numeric)  # Filtra solo columnas numéricas
    plt.savefig(pairplot_path, dpi=300, bbox_inches='tight')
    print(f"Gráficas de dispersión guardadas en: {pairplot_path}")
    plt.close()
