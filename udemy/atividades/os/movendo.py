import os

home= os.path.dirname(__file__)
complemento = "testeOS"
arquivo= "Artificial Intelligence – that doesn’t sound alright!.png"



origem = os.path.join(home,complemento,arquivo)
destino= os.path.join(home,arquivo)

os.rename(origem,destino)