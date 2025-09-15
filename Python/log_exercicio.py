import random
from datetime import datetime, timedelta

def gerar_logs_temporais(qtd_logs, inicio, intervalo_segundos):
    """
    Gera uma lista de logs simulados, onde cada  log possui um timestamp e um valor numérico.

    Args:
        qtd_logs(int): Quantidade de logs a serem gerados.
        incicio(datetime): Data e hora de inicio para o primeiro log.
        intervalo_segundos: Intervalo em segundos entre cada log.

    Retuns:
        list: Lista de logs simulados, onde cada log é um dicionário com as chaves "tempo e valor".


    """
    logs = []
    tempo_atual = inicio
    for _ in range(qtd_logs):
        valor = round(random.uniform(20.0, 80.0), 2)
        log = {"tempo": tempo_atual, "valor": valor}
        logs.append(log)
        tempo_atual += timedelta(seconds=intervalo_segundos)
    return logs 

def calcular_media_movel(logs, janela):
    """
    Calcula a média móvel para uma janela de tamanho 'janela' sobre a lista de logs.
    
    Args: 
        logs(float)
        janela()

    Returns:
        Retorna uma lista de dicionario com o timestamp correspondente à ultima leitura da janela
        e a média calculada para aquele intervalo.


    """
    media_moveis = []
    for i in range(len(logs)- janela + 1):
        soma = sum(log["valor"] for log in logs [i:i+janela])
        media = soma / janela
        registro_media = {"tempo": logs[i + janela - 1 ]["tempo"], "media":round(media, 2)}
        media_moveis.append(registro_media)
    return media_moveis    

def inserir_log(logs, novo_log, posicao=None):
    """
    Insere um novo log na lista 'logs'.
    Se a posição não for especificada ou for maior que o tamanho atual da lista,
    o log é adicionado ao final.

    Args:
        logs
        novo_log
        posicao

    Returns:


    """
    if posicao is None or posicao >= len(logs):
        logs.append(novo_log)
    else:
        logs.append(posicao, novo_log)
    return logs

def detectar_anomalias(medias_moveis, limite):
    """
    """
    anomalias = [registro for registro in medias_moveis if registro ["media"] > limite]
    return anomalias 

def main():

    inicio   = datetime.now()
    qtd_logs = 100 # numero de logs simulados
    intervalo_segundos  = 60 #intervalo de 60 segundos de cada log
    logs = gerar_logs_temporais(qtd_logs, inicio, intervalo_segundos)

    print("Exibindo os primeiros 5 logs gerados")
    for log in logs[:5]:
        print(f'{log['tempo']} - Valor: {log['valor']}')

    janela = 5 # Tamanho da janela para o cálculo da média móvel.
    medias_moveis = calcular_media_movel(logs, janela)

    print("\nExibindo as primeiras 5 médias móveis calculadas: ")
    for media in medias_moveis[:5]:
        print(f'{media['tempo']} - Média: {media['media']}')

    limite_anomalia = 70.0 #Limite no qual a media a cima disso é considerada uma anomalia.
    anomalias = detectar_anomalias(medias_moveis, limite_anomalia)
    print(f'\nQuantidade de anomalias detectadas (média móvel > {limite_anomalia}): {len(anomalias)}')

    #Inserindo um novo log simulando a atualização dos dados
    nova_data = logs[-1] ["tempo"] + timedelta(seconds=intervalo_segundos)
    novo_valor = round(random.uniform(20.0, 80.0), 2)
    novo_log   = {"tempo": nova_data, "valor": novo_valor}
    logs = inserir_log(logs, novo_log)
    print(f"\nNovo log inserido: {novo_log['tempo']} - Valor: {novo_log['valor']}")
    print(F'total de logs após inserção: {len(logs)}')

if __name__ == "__main__":
    main()     


