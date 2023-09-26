from pathlib import Path


base = Path(r"C:\Users\FARIAS\Desktop\tema1")


cont = 0
contd= 0
for item  in  base.iterdir():
    if item.is_file():

        cont = cont+1
        print(item.name)
    else:
        contd+=1


print(F"total de :{cont} arquivos")
print(F"total de :{contd} diretorio ")