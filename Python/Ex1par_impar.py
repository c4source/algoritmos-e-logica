def main():
    """""   
    função para verificar se um numero é impar ou par  

    função recebe um parametro (n) 
    numero de entrada colocado pelo usuario.

    retorna:
    a condição n % 2 == 0 retorna as condições em que se o numero de entrada
    é positivo ou falso (par ou impar) ele mostrará o resultado

    """""
    def impar_par(n):
        if n % 2 == 0:
            return("par")
        else:
            return("Impar") 
    entrada = int(input("Digite um numero inteiro: "))
    resultado = impar_par(entrada)
    print(f"O numero {entrada} é {resultado}")
if __name__ == "__main__":
    main()   
   
             
