NOME= input("DIGITE UM NOME")

with open ("ARQUIVO.TXT","w") as file:
    file.write(f"{NOME}\n")