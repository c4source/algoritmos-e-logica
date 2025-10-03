import json 

class Contatos():
    def __init__(self, nome, email, cpf, telefone):
        self.nome = nome
        self.email = email 
        self.cpf = cpf 
        self.telefone = telefone
        
    def to_dict(self):
        
        return {
            'nome':self.nome,
            'email':self.email,
            'cpf':self.cpf,
            'telefone':self.telefone, 
        }      

contato_1 = Contatos("Gabriel", "gabrielhenriques69@gmai.com", "cpf", "telefone") 

lista = []
lista.append(contato_1.to_dict())
print(lista)

with open("dados.json", "w") as arquivo:
    json.dump(lista,arquivo,indent=4)
    
#Atributos privados

import json 

class Contatos():
    def __init__(self, nome, email, cpf, telefone):
        self.__nome = nome
        self.__email = email 
        self.__cpf = cpf 
        self.__telefone = telefone
        
    def to_dict(self):
        
        return {
            'nome':self.__nome,
            'email':self.__email,
            'cpf':self.__cpf,
            'telefone':self.__telefone, 
        }      

contato_1 = Contatos("Gabriel", "gabrielhenriques69@gmai.com", "cpf", "telefone") 

lista = []
lista.append(contato_1.to_dict())
print(lista)

with open("dados.json", "w") as arquivo:
    json.dump(lista,arquivo,indent=4)
    



