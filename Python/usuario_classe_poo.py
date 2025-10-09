class Cliente():

    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano
        self.lista_planos = ["Basic", "Premium", "Master"]

        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido")   



    def mudar_plano(self, novo_plano):

        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano inválido")   

    def ver_filme(self, filme, plano_filme):

        if plano_filme == plano_filme:
            print(f"Ver filme {filme}")

        elif plano_filme == "Premium":
            print("Ver o filme {filme}") 

        elif plano_filme == "Basic" and self.plano == "Premium":
            print("Faça upgrade para o premium")
        else:
            print("Plano inválido")                    

cliente = Cliente("Gabriel", "Basic")
print(cliente.plano)
cliente.ver_filme("Django", "Premium")


#botao upgrade
cliente.mudar_plano("Premium")
print(cliente.plano)