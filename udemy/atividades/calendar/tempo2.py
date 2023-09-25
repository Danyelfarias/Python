import locale

locale.setlocale(locale.LC_ALL,"Pt_br.utf-8")

# import calendar
# mes,ano = map(int,input("digite um mes ano (mes/ano)").split("/"))
# calendario = calendar.month(ano,mes)

# for i,w in enumerate(calendar, start=1):
    
#     print ( f"semana {i} {w}")

import calendar

# Solicita ao usuário o ano e o mês
ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês (1 a 12): "))

# Obtém o nome do mês
nome_mes = calendar.month_name[mes]

# Obtém o calendário para o mês e ano especificados
calendario = calendar.monthcalendar(ano, mes)

# Define uma lista com os nomes dos dias da semana
dias_da_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

# Exibe o cabeçalho com os nomes dos dias da semana
for dia in dias_da_semana:
    print(f"{dia:<4}", end=" ")
print()

# Itera pelos dias do mês e exibe os números dos dias
for semana in calendario:
    for dia in semana:
        if dia == 0:
            print("    ", end=" ")  # Para os dias que não pertencem ao mês
        else:
            print(f"{dia:2d}  ", end=" ")
    print()  # Move para a próxima linha após cada semana