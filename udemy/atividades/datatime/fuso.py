# import datetime 
# from dateutil.relativedelta import relativedelta

# h=int(input("que horas é esse exato momento: "))
# partida_eua= datetime.datetime.now().replace(hour=h,minute=0,second=0)

# fuso=relativedelta(hours=13)
# chegada_toquio= partida_eua+fuso

# print(f"vc vai chegar em toqui as {chegada_toquio}")
import datetime
from dateutil.relativedelta import relativedelta

h = int(input("Que horas são neste momento (no horário de Nova York): "))

# Crie um objeto datetime para o horário de partida em Nova York
partida_eua = datetime.datetime.now().replace(hour=h, minute=0, second=0)

# Defina o deslocamento de 13 horas para Tóquio
fuso = relativedelta(hours=13)

# Calcule o horário de chegada em Tóquio adicionando o deslocamento ao horário de partida
chegada_toquio = partida_eua + fuso

print(f"Você vai chegar em Tóquio às {chegada_toquio.strftime('%H:%M')} (horário de Tóquio).")
