# Crie um programa que solicite uma data de nascimento e, em seguida, determine e exiba a data do próximo aniversário do usuário.

from datetime import datetime
from dateutil.relativedelta import relativedelta

dia, mes, ano = map(int, input("Qual é a sua data de aniversário (dia mês ano): ").split())

data_aniversario = datetime(ano, mes, dia)
um_ano = relativedelta(years=1)#mais preciso 
proximo_aniversario = data_aniversario + um_ano

fmt = '%d/%m/%Y' #para colocar no padrao brasiliero 
data_aniversario_formatada = proximo_aniversario.strftime(fmt) #strFtime  seria o 'f""' que a gente usar quando ja tem variavel para usar , ao inver se chamr direto no metood datetime.
print(f"Seu próximo aniversário será em {data_aniversario_formatada}")
