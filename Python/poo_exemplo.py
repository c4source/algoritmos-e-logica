# Exemplo de POO. 

class ControleRemoto():
    
    def __init__ (self, cor, altura, largura, profundidade):
        self.cor = cor 
        self.altura = altura
        self.largura = largura 
        self.profundidade = profundidade
    
    def passar_canal(self, botao):  
        
        if botao == ">":
            print("Passar canal para frente")
        elif botao == "<":
            print("Voltar canal para trás")
            
controle_remoto = ControleRemoto("Cinza", "10cm", "2cm", "2cm") 
print(f'cor: {controle_remoto.cor}')
print(f'altura: {controle_remoto.altura}')
print(f'largura: {controle_remoto.largura}')
print(f'profundidade: {controle_remoto.profundidade}')
controle_remoto.passar_canal("+")
controle_remoto2 = ControleRemoto("Preto", "10cm", "2cm", "2cm")


