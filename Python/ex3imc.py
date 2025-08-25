print(" \== Descubra seu IMC ==")
altura = float(input("Digite sua altura: "))
peso   = float(input("Digite seu peso em Kilo gramas: "))
imc    = peso / (altura * altura)
print (f"Seu imc é {imc:.2f}")
if imc < 18.5: 
    print("A baixo do peso ideal: ")
elif imc <= 24.9:
    print("Peso ideal")
elif imc <= 29.9:
    print("A cima do peso")
elif imc <= 34.9:
    print("Obesidade")
else:
    print("Obesidade morbida")
                 
