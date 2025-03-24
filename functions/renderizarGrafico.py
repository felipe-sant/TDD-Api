import matplotlib.pyplot as plt
from datetime import datetime

def renderizarGrafico(symbol, dados_filtrados):
    dias = []
    precos = []
    for data in dados_filtrados['dia']:
        data_obj = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%fZ')
        data_formatada = data_obj.strftime('%d/%m')
        dias.append(data_formatada)
    for preco in dados_filtrados['preco']:
        precos.append(preco)
    
    plt.plot(dias, precos, marker='o')
    plt.title(f'Ação da {symbol} ao longo do tempo')
    plt.xlabel('Tempo')
    plt.ylabel('Dinheiro')

    plt.show()