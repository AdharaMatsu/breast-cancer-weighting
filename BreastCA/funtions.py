
def print_dictToDict(dictionary):
    for template_id, info in dictionary.items():
        print(f"{template_id}:")
        for key, value in info.items():
            print(f"  {key}: {value}")
        print()  # línea en blanco entre entradas