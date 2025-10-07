class Veiculo():
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        
    def mover(self):
        print("O carro está se movendo")
        

class Carro(Veiculo):
    def mover(self):
        print(f'{self.modelo} está se movendo ')

class Moto(Veiculo):
    def mover(self):
        print(f'{self.modelo} ta se movendo')
        
carro = Carro("Preto", "Corolla", "2022")
moto  = Moto("Azul", "Hornet", "2019" )

veiculos = [carro, moto]

    
for i in veiculos:
    i.mover()
