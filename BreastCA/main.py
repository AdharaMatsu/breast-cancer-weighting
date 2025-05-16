import pandas as pd
import random
import json
import os

from funtions import print_dictToDict


def random_risk_factors(df, attributes_header):
    random_weighing = {}
    for attribute in attributes_header[:-1]:  # Sin count
        key = attribute
        dic_aux = {}
        unique_values = df[attribute].unique()
        for values in unique_values:
            rnd_value = random.randint(5, 16)
            dic_aux[int(values)] = rnd_value

        random_weighing[key] = dic_aux

    return random_weighing


def replace_values(df, replacements):
    df_processed = df.copy()

    for column, random_dict in replacements.items():
        replacement_series = df_processed[column].map(random_dict)
#        df_processed[column] = pd.DataFrame(replacement_series)
        df_processed[column] = replacement_series.combine_first(df_processed[column])  # Reemplaza solo valores existentes en el diccionario
    return df_processed

def add_column(df_processed):
    df_processed['suma'] = df_processed.iloc[:, 1:-1].sum(axis=1)
    return df_processed

def FO(df_processed):
    return df_processed['count'].corr(df_processed['suma'])

def write_json(filename, df_processed):
    with open(filename,'w') as f:
        json.dump(df_processed,f,indent=5)

def create_json(filename, df_procesed):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            json_results = json.load(f)
            join_results = {**df_procesed, **json_results}
            join_results = dict(sorted(join_results.items(), key=lambda x: x[1]['correlacion'], reverse=True)[:5])
        #write_json(filename, join_results)
        return json_results

    else:
        df_procesed = dict(sorted(df_procesed.items(), key=lambda x: x[1]['correlacion'], reverse=True)[:5])
        #write_json(file, df_procesed)
        return df_procesed

def convert_keys_to_int(d):
    new_dict = {}
    for k, v in d.items():
        if isinstance(v, dict):
            # Convierte claves del subdiccionario a int
            new_dict[k] = {int(sub_k): sub_v for sub_k, sub_v in v.items()}
        else:
            new_dict[k] = v
    return new_dict


if __name__ == "__main__":
    dataset_original = "Datasets/BCSC-risk_factors.csv"
    dataset_last_version = 'Last Project/HarmonyForBreastCancer/BCSC_risk_factors_153821.csv'
    dataset_process = 'Datasets/BCSC-dataset_153821_0325.csv'

    file = 'randoms_test.json'

    df_process = pd.read_csv(dataset_process)
    ids = df_process['id']
    df_process.drop('id', axis=1, inplace=True)
    header = df_process.columns
    results = {}

    random.seed(10)
    for e in range(10):
        random_replacements = random_risk_factors(df_process, header)
        df_replaced = replace_values(df_process, random_replacements)
        df_replaced = add_column(df_replaced)
        nueva_correlacion = FO(df_replaced)

        key_name = 'random test ' + str(e+1)
        results[key_name] = {
            'parametros': random_replacements,
            'correlacion': nueva_correlacion
        }
    best_random_results = create_json(file, results)

    # toma el diccionario
    test_result = best_random_results['random test 9']
    random_test = convert_keys_to_int(test_result['parametros'])
    correlacion_anterior = test_result['correlacion']

    rnd_probability = random.randint(1, 11)

    for attribute, value_dict in random_test.items():
        for subclave, subvalor in value_dict.items():
            if random.randint(1, 100) <= 50:
                value_dict[subclave] = subvalor + 2
            else:
                value_dict[subclave] = subvalor - 2


    df_replaced = replace_values(df_process,random_test)
    df_replaced = add_column(df_replaced)
    nueva_correlacion = FO(df_replaced)
    print(nueva_correlacion)









