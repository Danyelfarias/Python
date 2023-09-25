# Crie um programa que solicite ao usuário um ano e um mês e, em seguida, exiba o calendário mensal correspondente usando a biblioteca calendar.
import locale

locale.setlocale(locale.LC_ALL,"Pt_br.utf-8")

import calendar

mes,ano = map(int,input("digite mes/ano que vc quer exibir: ").split("/"))
calendario = calendar.month(ano,mes)
print(calendario)


