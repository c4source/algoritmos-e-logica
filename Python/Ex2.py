#Area do quadrado 
print("Descubra a area do retângulo.")
altura  = float(input("Digite a altura: "))
largura = float(input("Digite a largura: "))


def area_do_retangulo(largura, altura):
    return largura * altura
area = area_do_retangulo(largura, altura)
print(f"A area do retângulo é: {area:.2f}")
