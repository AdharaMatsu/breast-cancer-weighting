import pandas as pd
from sklearn import metrics

#leer archivo .csv
df = pd.read_csv('Diagnostico original - gail.csv')

#imprime los datos del dataframe
#print(df)

#obtiene las etiquetas reales y las etiquetas predichas
y_true = df['diagnosis'].values
y_predict = df['diagnosisG'].values

# Imprime la matriz de confusion
print(metrics.confusion_matrix(y_true, y_predict))
# Imprime las metricas como precision, sensibilidad, etc.
print(metrics.classification_report(y_true, y_predict))





