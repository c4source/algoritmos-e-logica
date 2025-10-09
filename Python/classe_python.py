class ControleRemoto():
    
    def __init__(self, cor, tamanho, largura, profundidade):
        self.cor = cor 
        self.tamanho = tamanho 
        self.largura = largura
        self.profundidade = profundidade 
    
    def passar_canal(self, botao):
        if botao == "+":
            print("Canal aumentado")
        elif botao == "-" :
            print("Canal diminuido")

controle_1 = ControleRemoto("Preto", "10c", "5cm", "2cm")
controle_2 = ControleRemoto("Branco", "12cm", "6cm", "3cm")


controle_1.passar_canal("+")
controle_2.passar_canal("-")



                     

