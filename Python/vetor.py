#Algoritmos de ordenação. 
#Bolha (Bubble Sort)

numeros = [5, 3, 8, 4, 2]

print("Vetor original: ", numeros)

for i in range(len(numeros)-1):
    for j in range(len(numeros)-1-i):
        if numeros[j]>numeros[j+1]:
            numeros[j], numeros[j+1]=numeros[j+1],numeros[j]

print("Vetor ordenado: ", numeros) 


#Fazer um algortimo de busca linear 
#Gerar um numero randomico no vetor
#Criar uma funcao p fzr uma busca linear 
#Se encontrou é zero, senao encontrou é 1


#Buscas: Linear (Sequencial), 
# Busca binária)

# dados = [5, 2, 1, 4, 3]

#Busca binária (Grande volume de dados)
#1 - ordenação
#2 - len(dados)/2 = 2,5  ---> func de fzr busca. Dividir pela metade o numero que vc deseja encontrar 

#27 do dez entregar as atividades 


