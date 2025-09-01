def main():

    print("\n Reajuste automatico de 15% do salário.")
    salario = float(input("Digite seu salário: "))
    porcentagem = salario * 0.15
    atualizado = salario + porcentagem
    print(f"Salário atual: {salario:.2f}")
    print(f"Salario com reajuste de 15%: {atualizado:.2f}")

if __name__ == "__main__":
    main()
