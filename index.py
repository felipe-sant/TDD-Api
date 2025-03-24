from dotenv import load_dotenv
import os
from functions.loadBronzeData import loadBronzeData
from functions.loadSilverData import loadSilverData
from functions.loadGoldData import loadGoldData
from functions.getGoldData import getGoldData
from functions.renderizarGrafico import renderizarGrafico

load_dotenv()
token = os.getenv('API_TOKEN')
symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NFLX", "NVDA", "PYPL", "SPOT", "SHOP"]

def main():
    # loadBronzeData(token, symbols)
    loadSilverData(symbols)
    loadGoldData()
    
    dados = getGoldData()
    
    execucao = True
    while execucao:
        try:    
            x=0
            print()
            print("Escolha uma das opções abaixo:")
            for symbol in symbols:
                print(f"{x} | Mostrar grafico - {symbol}")
                x+=1
            print("- | Digite para sair")
            print()
            
            opcao = input("digite sua opção: ")
            
            if opcao == "-":
                execucao = False
                
            symbol = symbols[int(opcao)]
            dados_filtrados = dados[dados['empresa'] == symbol]
            os.system('cls')
            renderizarGrafico(symbol, dados_filtrados)
            
            input()
        except:
            execucao = False
    
if __name__ == "__main__":
    main()