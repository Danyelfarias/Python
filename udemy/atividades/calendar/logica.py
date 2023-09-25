# : Crie um programa que calcule o número de dias úteis (dias da semana, excluindo fins de semana) em um mês específico de um ano fornecido pelo usuário usando a biblioteca calendar.

import locale

locale.setlocale(locale.LC_ALL,"Pt_br.Utf-8")



import calendar
d,m,a=map(int,input("escolha a data (12/08/2023)").split("/"))
dia_semana = calendar.weekday(a,m,d)


if dia_semana == 5 or dia_semana == 6 :
    print("esse dia é um final de semana") 