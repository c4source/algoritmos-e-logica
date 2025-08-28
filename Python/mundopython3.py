n1 = int(input("Numero: "))
n2 = int(input("Outro valor: "))
s = n1 + n2 
m = n1 * n2 
d = n1 / n2 
di = n1 // n2
e = n1 ** n2 

print('A soma é {}, a multiplicação é {}, a divisão é {:.3f}'.format(s, m, d)) 
print('A divisão inteira é {}, a exponeciação é {}'.format(di, e))
