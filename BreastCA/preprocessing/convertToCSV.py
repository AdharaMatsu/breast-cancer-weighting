import pandas as pd

# Read excel file (.xlsx)
route = "Datasets - Not use/bcbs 1.xlsx"
df = pd.read_excel(route)

# Save DataFrame such as CSV
route_csv = "Datasets/BCBS-dataset.csv"  # Define the route where save the dataset
df.to_csv(route_csv, index=False)  # `index=False` is for not include Devita incluir los índices del DataFrame como columna en el CSV

print(f"Archivo convertido y guardado en: {route_csv}")
