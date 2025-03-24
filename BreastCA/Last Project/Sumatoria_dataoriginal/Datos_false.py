import csv

data = {}

#Abrir el archivo "Soluciones optimasv2.csv" y leer su contenido
with open('Soluciones optimasv2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile) #delimiter='\t'
    # Iterar sobre cada fila en el archivo
    for row in reader:
        if len(row) > 1:
            key = float(row[0])
            value = int(row[1])
            # Almacenar el par clave-valor en el diccionario
            data[key] = value

# Leer los datos del archivo "dfFalse.csv" y reemplazar los valores
with open('dfFalse.csv', 'r') as infile, open('datos dfFalse_conSumatoria.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)  # Leer la primera fila como encabezado
    header.append("sumatoria")  # Agregar el nombre de la columna
    writer.writerow(header)

    # Variables para almacenar los valores máximo y mínimo
    max_value = float('-inf')
    min_value = float('inf')

    for row in reader:
        updated_row = []
        sumatoria = 0  # Variable para la sumatoria de los nuevos elementos generados
        for item in row:
            try:
                # Intentar convertir el valor a float y buscarlo en el diccionario
                key = float(item)
                #updated_row.append(data[key])
                updated_value = data[key]
                updated_row.append(updated_value)
                sumatoria += updated_value  # Agregar el valor a la sumatoria
            except ValueError:
                # El valor no se puede convertir a float, dejarlo sin cambios
                updated_row.append(item)
        updated_row.append(sumatoria)  # Agregar la sumatoria como nueva columna
        writer.writerow(updated_row)

        # Actualizar los valores máximo y mínimo
        max_value = max(max_value, sumatoria)
        min_value = min(min_value, sumatoria)

    print("Valor mínimo:", min_value)
    print("Valor máximo:", max_value)
    print("Datos correctamente guardados")
