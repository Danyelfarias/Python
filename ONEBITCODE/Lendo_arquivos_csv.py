with open ("arquivo.csv","w",encoding="utf-8") as arquivo:
    arquivo.write("teste, teste2")
with open ("arquivo.csv","r",encoding="utf-8") as arquivo:
    cont=0
    for linha in arquivo:
        row = linha.strip().split(",")
        print(row[cont])
        cont=cont+1
        print(row[cont])