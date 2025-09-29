# STRING


# nome_de_um_filha_da_puta = "GABRIEL HENRIQUE DOS SANTOS DOMINGUES"
# print(nome_de_um_filha_da_puta[:19])

# frase = "Viadinho do caralho"
# print(frase[9:10])

#slacing  pular em dois em dois
# frase = "Gabriel Henrique dos Santos Domingues"
# print(frase[9:21:2])

#Pular em 3 em 3
# frase = "Gabrie lHenrique dos Santos Domingues"
# print(frase[9::3])

#LEN
# frase = "Gabrie lHenrique dos Santos Domingues"
# print(len(frase))

#Contar quantas vezes um determinado caractere acontece
# frase = "Gabriel Henrique dos Santos Domingues"
# print(frase.count('o'))
# print(frase)

#Contar Qts x aparece o elemento da string especificando o começo e o final dos indices
# frase = "Gabriel Henrique dos Santos Domingues"
# print(frase.count('e', 0, 14))

#Mostra onde começa o indice especificado dentro do find()
# frase = "Gabriel Henrique dos Santos Domingues"
# print(frase.find('Gabriel'))

# -1 quando nao tiver dentro da string o que vc pediu
# frase = "Gabriel Henrique dos Santos Domingues"
# print(frase.find('Arroz'))

#Substituir o pedaço da string por outro 
# frase = "Gabriel Henrique dos Santos Domingues"
# print(frase.replace('Henrique', 'Silva'))

# Exercicios 
# 
# 22) Crie um programa que leia o nome completo de uma pessoa e mostre: 
# 

# nome = input('Digite um nome: ')

# def tudo_maiusculo(nome):
#     nome.upper(nome)
#     return tudo_maiusculo 


# def tudo_minusculo(nome):
#     nome.lower(nome)
#     return tudo_minusculo

# def comprimento_sem_espaço(nome):
#     nome.split(nome)
#     nome.len(nome)
#     return tudo_minusculo



# def total_de_letras(nome):
#     nome.len(nome)
#     return tudo_minusculo

# while True:

#     condicao_1 = int(input('Digite 1 para converter o nome para Maisculo> '))
#     if condicao_1 == 1:
#         print(tudo_maiusculo(nome))
#         break
#     else:
#         print('Comando Inválido.')

#     condicao_2 = int(input('Digite 2 para converter o nome para Minuscula> '))
#     if condicao_2 == 2:
#             print(tudo_minusculo)
#             break
#     else:
#          print('Comando inválido.')
#     condicao_3 = int(input('Digite 3 para ver quantas  letras tem o nome {nome}> '))
#     if condicao_3 == 4: 
#          print(comprimento_sem_espaço(nome))
#          break
#     else:
#          print('Comando inválido.')

#     condicao_4 = int(input('Digite 4 para ver quantas letras tem o nome {nome}> '))
#     if condicao_4 == 4:
#          print(total_de_letras(nome))
#          break
#     else:
#          print('Comando inválido.')
# 
# 



def tudo_maisculo(nome):
    return nome.upper() 

def tudo_minusculo(nome):
    return nome.lower()

def comprimento_sem_espaço(nome):
    return len(nome.replace(" ", " "))

def quantos_caracteres(nome):
    return len(nome)

nome = input('Digite um nome: ')

while True:

    print('\n=== MENU ===')
    print('1 - para converter tudo para maiuscula')
    print('2 - para converter tudo para minuscula')
    print('3 - para contar comprimento sem espaço')
    print('4 - para contar quantos caracteres tem a string:')
    print('5 - para Sair: ')

    try:
        opcao =int(input('Opção desejada: '))
    except ValueError:
        print('Opção Inválida.')
        continue 

    if opcao == 1:
        print(f'Maiusculo: {tudo_maisculo(nome)}')
        
    elif opcao == 2:
        print(f'MinusculO: {tudo_minusculo(nome)}')
    elif opcao == 3:
        print(f'Comprimento sem espaço: {comprimento_sem_espaço(nome)}')
    elif opcao == 4:
        print(f'Quantidade de caracterece: {quantos_caracteres(nome)}')
    elif opcao == 5:
        print('Saindo...')
        break
    else:
        print('Comando inválido.')    

     






