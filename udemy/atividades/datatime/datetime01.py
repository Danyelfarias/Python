

from datetime import datetime

# dia_aniversario = int(input("Digite o dia do aniversário: "))
# mes_aniversario = int(input("Digite o mês do aniversário: "))
# ano_aniversario = int(input("Digite o ano do aniversário: ")) maneira usual 

dia_aniversario, mes_aniversario, ano_aniversario = map(int, input("Digite a data de aniversário (dia mês ano): ").split())
#map é o que possibiliata o imput aumentar seu poder/split vai torna uma lista de iten apartir dos espaços


data_1= datetime(ano_aniversario,mes_aniversario,dia_aniversario)#lembrar sempre ano--> mes --> dia --> hora --> min--> seg
fmt = '%d.%m.%Y'#nao esquecer de colocar o % sempre na frente das formataçoes

dataformatada= datetime.strftime(data_1,fmt)#quando é strFtime ,precisa de dois argumentos e ele faz parte da biblioteca "datetime"
# o comando vem dele ^^^^^^^^^(OLHA PRA CIMA DAS SETA ANTERIORES)

print(dataformatada)

