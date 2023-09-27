import PyPDF2
from pathlib import Path
def extract_page_from_pdf(filename, page_number, output_filename):
    with open(filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        writer = PyPDF2.PdfWriter()
        writer.add_page(reader.pages[page_number - 1])
        
        with open(output_filename, 'wb') as output_file:
            writer.write(output_file)

def find_and_extract_word_in_pdf(filename, target_word):
    with open(filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            
            if target_word in text:
                output_filename = Path(fr"C:\Users\FARIAS\Desktop\Nova pasta\pagina_{page_number}.pdf")
                extract_page_from_pdf(filename, page_number, output_filename)
                return page_number, output_filename
    
    return None, None

# Exemplo de uso
filename = Path(r"C:\Users\FARIAS\Desktop\DT Hosp CE 21.09.2023.pdf")

target_word = str(input("digite a nota ou a dt"))#dt que eu quero encontra

page_number, extracted_file = find_and_extract_word_in_pdf(filename, target_word)
if page_number:
    print(f"A palavra '{target_word}' foi encontrada na página {page_number}.")
    print(f"A página {page_number} foi extraída e salva como '{extracted_file}'.")
else:
    print(f"A palavra '{target_word}' não foi encontrada no PDF.")