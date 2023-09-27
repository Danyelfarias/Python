from PIL import Image
from pdf2image import convert_from_path
from PyPDF2 import PdfWriter
from pathlib import Path

def convert_to_searchable_pdf(pdf_path, output_path):
    # Converte as páginas do PDF em imagens
    images = convert_from_path(pdf_path)

    # Cria um objeto PdfWriter para escrever o PDF pesquisável
    writer = PdfWriter()

    for image in images:
        # Converte a imagem em escala de cinza
        image = image.convert("L")

        # Adiciona a imagem ao PDF pesquisável
        writer.add_page()
        writer.addImage(image)

    # Salva o arquivo PDF pesquisável
    with open(output_path, "wb") as f:
        writer.write(f)

# Exemplo de uso
pdf_path = Path(r"C:\Users\FARIAS\Desktop\DT Hosp CE 21.09.2023.pdf")
output_path = Path(r"C:\Users\FARIAS\Desktop\Nova pasta\copia.pdf")

# Chamada da função para converter o PDF
convert_to_searchable_pdf(pdf_path, output_path)
