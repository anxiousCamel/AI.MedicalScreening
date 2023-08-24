#data_loading

import json
import os

"""
Carrega os dados de um arquivo JSON.

Parâmetros:
filename (str): O nome do arquivo JSON a ser carregado.

Retorna:
dict: Os dados carregados do arquivo JSON ou None se o arquivo não for encontrado.
"""
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
    else:
        print(f"O arquivo '{filename}' não foi encontrado.")
        return None