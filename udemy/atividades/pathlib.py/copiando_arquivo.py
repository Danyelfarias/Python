import shutil
from pathlib import Path

arquivo = Path(r"C:\Users\FARIAS\Desktop\tema1\INVISIVEL1.jpg")
arquivo_destino = Path(r"C:\Users\FARIAS\Desktop\tema1\arquivosaleatorio_1_1_1\copiado.jpg")

# Copiar o arquivo de origem para o destino
shutil.copy(arquivo, arquivo_destino)
