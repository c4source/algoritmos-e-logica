# Pilhas & Filas

# --->  pilhas (lifo: Ultimo a sair e primeiro a ser colocado) #pop
# ---> filas  ( Fifo: O primeiro sera o ultimo a ser colocado) #append

# FILA: append()
# PILHA: #Pop(0), #append 
#FILA
def main():
     fila = []
     print(f'Lista vazia: {fila}')
     fila.append(3)
     print(f'{fila =}')
     fila.append(5)
     print(f'{fila =}')
     fila.append(7)
     print(f'{fila =}')
     fila.append(9)
     print(f'{fila =}')
     print(f"Lista atualizada: {fila}")
     fila.pop(0)
     print(f'Lista com elemento removido: {fila}')
     fila.append(11)
     print(fila)
if __name__ == "__main__":
    main()    

#PILHA
def main():
    
    pilha = []
    print(pilha)
    pilha.insert(0, 3) # remover o primeiro indice e adicionar o elemento que tu quer: 3 
    print(pilha)
    pilha.insert(0, 5)
    print(pilha)
    pilha.insert(0, 7)
    print(pilha)
    pilha.insert(0, 9)
    print(pilha)
    pilha.pop(0)
    
    
if __name__ == "__main__":
    main()

