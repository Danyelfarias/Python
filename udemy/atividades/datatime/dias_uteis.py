# Escreva uma função que determine a quantidade de dias úteis (dias da semana, excluindo fins de semana) em um intervalo de datas.

from datetime import datetime
import calendar
import locale
locale.setlocale(locale.LC_ALL,"Pt_br.Utf-8")

dia,mes,ano= map(int,input("digite a primetia data: ").split("/"))
dia2, mes2 , ano2= map(int,input("digite a segunda data: ").split("/"))


data_1 = datetime( ano,mes,dia)
data_2 = datetime( ano2,mes2,dia2)


data_formatada1= data_1.strftime("%d.%m.%Y") 
data_formatada2= data_2.strftime("%d.%m.%Y") 



difenca= data_formatada1-data_formatada2
cont = 0
for i in calendar.weekday(difenca):
    if i != 5 or i!= 6 :
        next
    else:
        cont= cont+1   

print(cont)