def main():
    print("\n == Aplique 5% de desconto ==")
    produto  = float(input("Coloque o preço: ")) #   x * 0.05 
    desconto = produto * 0.05
    produtoCmDesconto = produto - desconto
    print(f"Valor do produto: {produto:.2f}")
    print(f"Valor com 5% de desconto: {produtoCmDesconto:.2f}")



if __name__ == "__main__":
    main()    
