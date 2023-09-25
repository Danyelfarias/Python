
# Desenvolva um programa que calcule o tempo decorrido em anos, meses e dias desde um evento específico (por exemplo, a data de nascimento de alguém ou o início de um projeto).

from datetime import datetime 




data_evento = input("qual foi o dia do ocorrido: (ANO/MES/DIA)")

data_fmt = datetime.strptime(data_evento,"%Y/%m/%d") #RECEBENDO EM STRING E FORMATADNO PARA FOMATO DE DATA EUROPEIA

# data_formatada = data_fmt.strftime("%d/%m/%Y") #FOMRATANDO PARA BRASILEIRO

hj= datetime.now()

diferenca= hj-data_fmt

anos = diferenca.days // 365
meses = (diferenca.days % 365) // 30
dias = (diferenca.days % 365) % 30

print(f"Tempo decorrido: {anos} anos, {meses} meses, {dias} dias")