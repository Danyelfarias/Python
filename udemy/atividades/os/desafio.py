
# Escreva um programa que mova arquivos de um diretório para outro com base em sua data de modificação. Por exemplo, 
# mova todos os arquivos modificados nos últimos 7 dias para um diretório de backup.

import os
import shutil
from datetime import datetime, timedelta

# Diretório de origem e destino
diretorio_origem = '/caminho/do/diretorio/origem'
diretorio_destino = '/caminho/do/diretorio/destino'

# Quantidade de dias para verificar
dias_para_verificar = 7

# Calcula a data limite para considerar os arquivos
data_limite = datetime.now() - timedelta(days=dias_para_verificar)

# Lista os arquivos no diretório de origem
for arquivo in os.listdir(diretorio_origem):
    caminho_arquivo = os.path.join(diretorio_origem, arquivo)
    
    # Verifica se o arquivo foi modificado nos últimos 7 dias
    data_modificacao = datetime.fromtimestamp(os.path.getmtime(caminho_arquivo))
    if data_modificacao > data_limite:
        
        # Move o arquivo para o diretório de destino
        shutil.move(caminho_arquivo, os.path.join(diretorio_destino, arquivo))
        print(f'Movido: {arquivo}')

print('Concluído.')