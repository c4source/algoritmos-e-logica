#Ordenação usando bubble sort em python
array = [2, 3, 4, 6, 7, 9, 5, 11]

print("Vetor inicial: ", array)

        #O loop externo garante o numero correto de passagens
for i in range(len(array)-1):
        #O loop interno faz as comparações e a otimização 
    for j  in range(len(array)-1-i):
        if array[j]>array[j+1]:
            #Comparação e troca, se o elemento atua for maior que o proximo eles são trocados.
            array[j], array[j+1] = array[j+1], array[j]

print("Vetor ordenado: ", array)


