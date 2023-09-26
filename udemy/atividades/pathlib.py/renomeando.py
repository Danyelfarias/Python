from pathlib import Path


caminho = Path(r"C:\Users\FARIAS\Desktop\tema1")

cont= 1
for item in caminho.iterdir():
    if item.is_file():
        novo_nome = caminho.joinpath(f"{item.name}_{cont}")
        item.rename(novo_nome)
        cont+=1


