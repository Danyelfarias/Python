# Desenvolva um programa que verifique um diretório e seus subdiretórios em busca de arquivos duplicados. Liste os arquivos duplicados e seus caminhos.

import os

home = r"C:\\Users\\FARIAS\\Downloads\\testeOS"
existente = []  # Initialize an empty list to store duplicate files

# Create a dictionary to store file names as keys and their full paths as values
file_dict = {}

# Walk through the directory and its subdirectories
for root, _, files in os.walk(home):
    #root = caminho todo menos pasta anterio ao arquivo, _ = pasta anterio ao arquivo , files = arquivo
    for filename in files:
        full_path = os.path.join(root, filename)

        # Check if the filename already exists in the dictionary
        if filename in file_dict:
            # If it exists, append the current and existing paths to the list of duplicates
            existente.append((filename, full_path, file_dict[filename]))
        else:
            # If it doesn't exist, add it to the dictionary with its full path
            file_dict[filename] = full_path

# Print the list of duplicate files
if existente:
    print("Duplicate files found:")
    for filename, current_path, existing_path in existente:
        print(f"File: {filename}")
        print(f"Current Path: {current_path}")
        print(f"Existing Path: {existing_path}")
else:
    print("No duplicate files found.")
