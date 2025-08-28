# Area do circulo 
# Pi * R²
import math 
r = float(input("Qual o raio do circulo: ")) 

""" Calculo da area de um circulo 

Está função recebe um numero de entrada
E realiza a equação PI * r² 

Args
    r (float): Numero de entrada para achar area do circulo
        
returns:
    float: A area do circulo pi * R²
    
"""

def area_circulo(r):
   return math.pi * (r ** 2)
resultado = area_circulo(r)

print (f"A area do circulo é: {resultado:.2f}")
