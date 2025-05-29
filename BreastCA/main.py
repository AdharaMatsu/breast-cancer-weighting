import pandas as pd
import random

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

    return new_correlation, df_replacements

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

    for _, random_replace in random_test.items():
        for attribute, values in random_replace.items():
            random_A = random.randint(1, 6)
            random_B = random.randint(1, 6)
            while random_A == random_B:
                random_B = random.randint(1, 6)

            random_replace[attribute] = values + random_A
            














