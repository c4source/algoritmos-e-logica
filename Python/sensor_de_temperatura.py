# import random 

# """
# função que 

# """

# def gerar_dados_sensor(qtd_leituras):
#    dados_sensor = [round(random.uniform(15.0, 35.0), 2) for _ in range(qtd_leituras)]
#    return dados_sensor

# def main():
#     quantidade_leituras = 10_000
#     dados = gerar_dados_sensor(quantidade_leituras)
#     print(f'Quantidade de leituras geradas: {len(dados)}') 
#     print(f'{dados[3]=}')
#     print(f'{dados[9999]=}')

# if __name__ == "__main__":
#     main()

# 

import random

def gerar_dados_sensor(qtd_leituras):
    dados_leitura = [round(random.uniform(1.0, 9998.0), 2) for _ in range(qtd_leituras)]
    return dados_leitura

def main():
    quantidade_leitura = 10_000
    dados = gerar_dados_sensor(quantidade_leitura)
    print(f'Quantidade de leituras: ', {len(dados)})
    print(f'{len(dados)}')
    print(f'{dados[152]}')
    print(f'{dados[1_000]}')




if __name__ == "__main__":
    main()    