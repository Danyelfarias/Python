import PyPDF2
from pathlib import Path
def find_word_in_pdf(filename, target_word):
    with open(filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            
            if target_word in text:
                return page_number
    
    return None

# Exemplo de uso
filename = Path(r"C:\Users\FARIAS\Desktop\DT Hosp CE 21.09.2023.pdf")
target_word = '173799'#dt que eu quero encontra

page_number = find_word_in_pdf(filename, target_word)
if page_number:
    print(f"A palavra '{target_word}' foi encontrada na página {page_number}.")
else:
    print(f"A palavra '{target_word}' não foi encontrada no PDF.")


