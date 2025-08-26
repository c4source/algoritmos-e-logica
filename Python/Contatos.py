import json
import os 

arquivo_contatos = "contatos.json"

def carregar_contatos():
    if os.path.exists(arquivo_contatos):
        try:
            with open(arquivo_contatos, 'r', encoding="utf-8")as arquivo:
                return json.load(arquivo )
        except json.JSONDecodeError:
            print("Erro ao carregar arquivo")
            return()
        return()


contatos = carregar_contatos()

for contato in contatos: # pyright: ignore
    print(f"nome: {contato['nome']}, celular: {contato['celular']}")
