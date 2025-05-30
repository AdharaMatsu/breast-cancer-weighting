import pandas as pd
import random
import copy

from funtions import print_dictToDict


def random_risk_factors(df, attributes_header):
    random_weighing = {}
    for attribute in attributes_header[:-1]:
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
        df_processed[column] = replacement_series.combine_first(df_processed[column])
    return df_processed

def add_column(df_processed):
    df_processed['sum'] = df_processed.iloc[:, 1:-1].sum(axis=1)
    return df_processed

def objective_function(df_processed):
    return df_processed['count'].corr(df_processed['sum'])

def get_sample(df, size_sample):
    sample_A = df[df['count'] == 0].sample(n=size_sample, random_state=42)
    sample_B = df[df['count'] == 1].sample(n=size_sample, random_state=42)

    # opcional: mezclar
    sample = pd.concat([sample_A, sample_B]).sample(frac=1, random_state=42)

    return sample

def best_results(results, times):
    best_tests = {}

    for _ in range(times):
        best_test_key = max(results, key=lambda test_name: results[test_name]['correlation'])
        best_tests[best_test_key] = results.pop(best_test_key)

    return best_tests

def evaluation(df, replacements):
    df_replacements = replace_values(df,replacements)
    df_replacements = add_column(df_replacements)
    new_correlation = objective_function(df_replacements)

    return new_correlation

if __name__ == "__main__":
    dataset_original = "Datasets/BCSC-risk_factors.csv"
    dataset_last_version = 'Last Project/HarmonyForBreastCancer/BCSC_risk_factors_153821.csv'
    dataset_process = 'Datasets/BCSC-dataset_153821_0325.csv'

    file = 'randoms_test.json'

    df_process = pd.read_csv(dataset_process)
    ids = df_process['id']
    df_process.drop('id', axis=1, inplace=True)
    header = df_process.columns

    random.seed(10)
    results_random_test = {}

    for repeat_count in range(10):
        random_replacements = random_risk_factors(df_process,header)
        correlation = evaluation(df_process, random_replacements)

        key_name = 'random test ' + str(repeat_count + 1)
        results_random_test[key_name] = {
            'parameters': random_replacements,
            'correlation': correlation
        }

    best_random_results = best_results(results_random_test,5)

    # random test 10, 5, 3, 7, 6
    test_result = best_random_results['random test 10']
    random_test = test_result['parameters']
    previous_correlation = test_result['correlation']

    df_process_sample = get_sample(df_process, 200)

    results = {}

    for attribute, value_dict in random_test.items():
        for subclave, subvalor in value_dict.items():
            add1 = random.randint(1, 5)
            add2 = random.randint(1, 5)
            while add1 == add2:
                add2 = random.randint(1, 5)

            cambios = [add1, add2, -add1, -add2]
            candidatos = []

            for cambio in cambios:
                nueva_config = copy.deepcopy(random_test)
                nueva_config[attribute][subclave] = subvalor + cambio

                score = evaluation(df_process_sample, nueva_config)

                test_name = f"{cambio}"
                resultados = {
                    'correlation': score,
                    'replacements': copy.deepcopy(nueva_config)
                }

                results[test_name] = resultados
                candidatos.append((score, cambio, nueva_config))

            # Elegir el mejor de los 4 y aplicar al random_test actual
            mejor_score, mejor_cambio, mejor_config = max(candidatos, key=lambda x: x[0])
            random_test[attribute][subclave] = subvalor + mejor_cambio
    top_tests = best_results(results, times=1)
    print_dictToDict(top_tests)

















