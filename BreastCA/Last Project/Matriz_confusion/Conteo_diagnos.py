import pandas as pd
from sklearn import metrics

#leer archivo .csv
df = pd.read_csv('Diagnostico original - gail.csv')

#imprime los datos del dataframe
#print(df)

#imprime el numero de elementos que hay en cada clase de la columna "diagnosis"
print(df['diagnosis'].value_counts())
#imprime el numero de elementos que hay en cada clase de la columna "diagnosisG"
print(df['diagnosisG'].value_counts())