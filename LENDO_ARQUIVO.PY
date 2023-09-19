with open("ARQUIVO.TXT","r",encoding="utf-8") as arquivo:#encoding="utf-8" serve para aceitar caracteres especiais como o "ç"
    for linha in arquivo:
        print(linha.rstrip())#rstrip() serve para reduzir espaçoes de uma linha para outra
