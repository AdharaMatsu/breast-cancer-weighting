from pathlib import Path

folder_path = Path('../Datasets')
filenames = []
names = [file.name for file in folder_path.iterdir() if file.is_file() and
         (file.suffix == '.csv' or file.suffix == '.data')]

for e in names:  # Create a List of tuples with names and filenames
    temp1 = e.split('-')
    temp = (temp1[0], e)
    filenames.append(temp)

