import os

home = os.path.dirname(__file__)#saber a base do caminho 

complemento = "testeOS"

caminho = os.path.join(home,complemento) #juntando caminhos 
for pasta in os.listdir(caminho):#usando listdir para saber o contudo da psta de forma noa recursiva
    print(pasta)


