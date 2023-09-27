# Desenvolva um programa que determine a diferença entre um caminho absoluto e um caminho relativo, incluindo a forma como eles são resolvidos.

# from pathlib import Path


# def  direrenca_de_caminho (caminho_absoluto, caminho_relativo):
#     relativo = Path(caminho_relativo).resolve()#torna agora um caminho absoluto


#     absoluto = Path(caminho_absoluto)

#     diferenca = relativo.relative_to(absoluto)

#     return diferenca


# caminho = Path(__file__)
# caminho_2= Path("FARIAS\Desktop\tema1")
# resultado = direrenca_de_caminho(caminho,caminho_2)
# print(f'Diferença entre o caminho absoluto e o caminho relativo: {resultado}')


from pathlib import Path

def diferenca_de_caminho(caminho_absoluto, caminho_relativo):
    relativo = caminho_relativo.resolve()  # Transforma em caminho absoluto

    absoluto = caminho_absoluto

    diferenca = relativo.relative_to(absoluto)

    return diferenca

# Substitua esses caminhos pelos caminhos absolutos ou relativos desejados
caminho = Path("/caminho/absoluto")
caminho_2 = Path("caminho/relativo")

resultado = diferenca_de_caminho(caminho, caminho_2)
print(f'Diferença entre o caminho absoluto e o caminho relativo: {resultado}')
