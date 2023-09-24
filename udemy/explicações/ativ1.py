#1000 emprestimo
#5 anos de pagamento
#data da retirada 20/12/2020
#venci dia 20 de cada mes


from datetime import datetime,timedelta
import dateutil

fmt= '%d/%m/%Y'
data_emprestimo = '20/12/2023'
data_emprestimo= datetime.strptime(data_emprestimo,fmt)
data_final= data_emprestimo+timedelta(days= 365)

