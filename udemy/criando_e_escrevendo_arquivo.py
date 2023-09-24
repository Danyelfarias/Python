filme={'titulo': 'O Senhor dos Anéis: A Sociedade do Anel', 
 'ano': 2001, 
 'diretor': 'Peter Jackson', 
 'genero': ['Aventura', 'Fantasia'], 
 'atores': [{'nome': 'Elijah Wood', 'personagem': 'Frodo Baggins'},
             {'nome': 'Ian McKellen', 'personagem': 'Gandalf'}, 
             {'nome': 'Viggo Mortensen', 'personagem': 'Aragorn'}], 
'classificacao': 'PG-13', 'duracao': 178}


print(__file__)


import os
import json

caminho_absoluto= os.path.abspath (

      os.path.join(  os.path.dirname(__file__),"arquivo_novo.json")

)

print(caminho_absoluto)
with open (caminho_absoluto,"w") as arquivo_x:
    json.dump(filme,arquivo_x,ensure_ascii=False,indent=2)

