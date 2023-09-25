# Escreva um programa que solicite duas datas de nascimento e calcule a diferença de idade em dias entre as duas datas.

from datetime import datetime

# fmt= '%Y.%m.%d'
fmt = '%Y.%m.%d'
agora = datetime.now().date()#usado quando eu quero somente a data. sendo que tem hora munuto segundo diponiveis
# data_1 = agora.strftime(fmt) #quando o comando ele é strFtime so precisa de um argomento ,que é a formataçao e ele é um METODO ou seja , age na variavel 
# (olhe p/)^^^^^^^^^^^


dia,mes,ano= map(int,input("sua data de aniversario: ").split())
date_2= datetime(ano,mes,dia).date()

# data_2=datetime.strptime(date_2,fmt) como nesse questao nao vai precisar converter data pq o importante é os dias ,entoa essa linha é desnecessaria.

diferença_dias=(agora-date_2).days

print(diferença_dias)

