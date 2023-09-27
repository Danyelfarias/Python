from pathlib import Path

caminho = Path(r"C:\Users\FARIAS\Desktop\tema1")

lista = []

for item in caminho.iterdir():
    if item.is_file():
        tamanho_bytes = item.stat().st_size
        tamanho_kb = tamanho_bytes / 1024  # Convertendo bytes para kilobytes
        nome = item.name
        lista.append((nome, tamanho_kb))

# Ordenar a lista pelo tamanho (em kilobytes)
lista_ordenada = sorted(lista, key=lambda x: x[1])

for nome, tamanho_kb in lista_ordenada:
    print(f"Nome do arquivo: {nome}, Tamanho: {tamanho_kb:.2f} KB")

