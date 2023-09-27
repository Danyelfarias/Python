
# ..........stackoverflow.............
# from pathlib import Path
# dt= Path(r"C:\Users\FARIAS\Desktop\DT Hosp CE 21.09.2023.pdf")
# import PyPDF2
# pdf_file = open(dt,'rb')
# pdf_reader = PyPDF2.PdfReader(pdf_file)
# page = pdf_reader.pages[1]
# text = page.extract_text()
# print(text)



from pathlib import Path
import PyPDF2

# Caminho para o arquivo PDF
dt = Path(r"C:\Users\FARIAS\Desktop\DT Hosp CE 21.09.2023.pdf")

# Abra o arquivo PDF em um contexto 'with' para garantir que seja fechado corretamente
with open(dt, 'rb') as pdf_file:
    # Crie um objeto PdfFileReader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Obtenha o número de páginas
    numero_de_paginas = len(pdf_reader.pages)

# Imprima o número de páginas
print(f"O arquivo PDF tem {numero_de_paginas} páginas.")
