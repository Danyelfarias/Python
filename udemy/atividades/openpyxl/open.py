from pathlib import Path

from openpyxl import Workbook

path_work= Path(__file__).parent
print(path_work)
path_save= Path(path_work/'arquivo.xlsx')



workbook = Workbook()
Worksheet= workbook.active




# Criando os cabeçalhos
Worksheet.cell(1, 1, 'Nome')
Worksheet.cell(1, 2, 'Idade')
Worksheet.cell(1, 3, 'Nota')

students = [
    # nome      idade nota
    ['João',    14,   5.5],
    ['Maria',   13,   9.7],
    ['Luiz',    15,   8.8],
    ['Alberto', 16,   10],
]


# for i, student_row in enumerate(students, start=2):
#     for j, student_column in enumerate(student_row, start=1):
#         worksheet.cell(i, j, student_column)

for student in students:
    Worksheet.append(student)

workbook.save(path_save)