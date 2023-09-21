from datetime import datetime

data = datetime(2023,4,9)# ano, mes, dia , horas, minutos, segundos

print(data)


formatacao= '%Y.%m.%d'#nome desse argumento é "DIRETIVAS"

data_formatada=data.strftime(formatacao)

print(data_formatada)