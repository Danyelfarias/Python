import csv
from pathlib import Path

caminho_csv = Path(__file__).parent / 'arquivo_csv.csv'

with open(caminho_csv, "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    
    # Iterar pelas linhas do arquivo CSV
    for linha in leitor:
        print(linha)

# import csv
# from pathlib import Path

# caminho_csv = Path(__file__).parent / 'arquivo_csv.csv'

# # Lista de cabeçalhos
# cabecalhos = ["pais", "australia", "inglaterra", "brasil"]

# # Abre o arquivo CSV para escrita
# with open(caminho_csv, 'w', newline='') as arquivo:
#     # Cria um objeto DictWriter
#     escritor = csv.DictWriter(arquivo, fieldnames=cabecalhos)
    
#     # Escreve o cabeçalho no arquivo
#     escritor.writeheader()
    
#     # Exemplo de escrita de dados no CSV (substitua pelo seu próprio código)
#     escritor.writerow({"pais": "Argentina", "australia": "Sim", "inglaterra": "Não", "brasil": "Sim"})
#     escritor.writerow({"pais": "Canadá", "australia": "Sim", "inglaterra": "Sim", "brasil": "Não"})
