# from pathlib import Path

# path_origem= Path(r"C:\Users\FARIAS\Desktop\tema1").resolve()


# # for ps in path_origem.iterdir():
# #     if subps.is_dir():
# #         for subps in ps.iterdir()
        
# for ps in path_origem.iterdir():
#     while ps.is_dir() :
#         cont = 0
#         for subps in ps:
#             cont= cont+1


# print(cont)
from pathlib import Path

def encontrar_caminho_mais_longo(diretorio, caminho_atual=Path()):
    if diretorio.is_file():
        return caminho_atual
    caminho_maximo = caminho_atual
    for subitem in diretorio.iterdir():
        if subitem.is_dir():
            caminho_novo = encontrar_caminho_mais_longo(subitem, caminho_atual=subitem)
            if len(caminho_novo.parts) > len(caminho_maximo.parts):
                caminho_maximo = caminho_novo
    return caminho_maximo

caminho_base = Path(r"C:\Users\FARIAS\Desktop\tema1")  # Substitua pelo seu caminho base
caminho_mais_longo = encontrar_caminho_mais_longo(caminho_base)

if caminho_mais_longo:
    numero_de_diretorios_aninhados = len(caminho_mais_longo.parts) - len(caminho_base.parts)
    print(f'Caminho mais longo: {caminho_mais_longo}')
    print(f'Número de diretórios aninhados: {numero_de_diretorios_aninhados}')
else:
    print('Nenhum diretório encontrado.')
