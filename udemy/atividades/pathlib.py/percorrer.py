# Crie um programa que percorra um diretório e seus subdiretórios em busca de arquivos com uma extensão específica (por exemplo, .txt) usando o pathlib.


from pathlib import Path


path_origem= Path(r"C:\Users\FARIAS\Desktop\tema1").resolve()



for parte_c in path_origem.iterdir():

    if parte_c.is_file():
        if parte_c.suffix==".txt":
            print(f"o arquivo {parte_c} é um arquvio txt")
        

