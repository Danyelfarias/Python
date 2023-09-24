
string_json= '''

{
    "titulo": "O Senhor dos Anéis: A Sociedade do Anel",
    "ano": 2001,
    "diretor": "Peter Jackson",
    "genero": ["Aventura", "Fantasia"],
    "atores": [
        {
            "nome": "Elijah Wood",
            "personagem": "Frodo Baggins"
        },
        {
            "nome": "Ian McKellen",
            "personagem": "Gandalf"
        },
        {
            "nome": "Viggo Mortensen",
            "personagem": "Aragorn"
        }
    ],
    "classificacao": "PG-13",
    "duracao": 178
}


'''
import json
from typing import TypedDict

class movie(TypedDict):
    titulo: str
    ano: int
    diretor: str
    genero: str
    atores: str
    classificacao: str
    duracao: float

filme: movie= json.loads(string_json)
# anofilme=filme["ano"]
# print(anofilme)
print(filme)