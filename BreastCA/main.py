
import pandas as pd
import random

def risk_factors(df, attr_header): #Asigna randoms
    list_attr = []
    for column in attr_header:
        dic_aux = {}
        unique_values = df[column].unique()
        for values in unique_values:
            rnd_value = random.randint(5, 16)
            dic_aux[int(values)] = rnd_value
        list_attr.append(dic_aux)

    return list_attr

def transpose_with_dict(df, dict, filename): # Asigna valores a dataset
    for i in range(len(df)):
        row = df.iloc[i].tolist()
        aux = 0
        for e in range(1,len(row)):
            searching_item = dict[aux].get(row[e], None)
            row[e] = searching_item
            aux = aux + 1
        df.iloc[i] = row

    df_process.to_csv(filename, index=False)

if __name__ == "__main__":
    dataset_original = "Datasets/BCSC-risk_factors.csv"
    dataset_last_version = 'Last Project/HarmonyForBreastCancer/BCSC_risk_factors_153821.csv'
    dataset_process = 'Datasets/BCSC-dataset_153821_0325.csv'

    df_process = pd.read_csv(dataset_process)
    ids = df_process['year']
    df_process.drop('year',axis=1)
    header = df_process.columns

    #random.seed(10)
    dic_attributes = risk_factors(df_process,header)
    transpose_with_dict(df_process,dic_attributes, 'GRASP_Test.csv')
    
