from dotenv import load_dotenv
import os
from functions.loadBronzeData import loadBronzeData
from functions.loadSilverData import loadSilverData
from functions.loadGoldData import loadGoldData
from functions.getGoldData import getGoldData
from functions.renderizarGrafico import renderizarGrafico

load_dotenv()
# token = os.getenv('API_TOKEN')
token = "uaLZdcM7SjyWJcrkSV09jS4CKzvm7VThCfznDaYN"
symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NFLX", "NVDA", "PYPL", "SPOT", "SHOP"]

def main():
    # loadBronzeData(token, symbols) # Há um problema na API, caso faça muitas requisições o token é bloqueado
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
            print("- | Para ver todos dados em tabela")
            print("= | Para sair")
            print()
            
            opcao = input("digite sua opção: ")
            
            if opcao == "-":
                x=1
                for s in symbols:
                    print(f"\n{s}:")
                    print(dados[dados['empresa'] == s])
                    input(f"\n{x}/{len(symbols)}")
                    x+=1
                continue
            elif opcao == "=":
                execucao = False
            else:
                symbol = symbols[int(opcao)]
                dados_filtrados = dados[dados['empresa'] == symbol]
                os.system('cls')
                renderizarGrafico(symbol, dados_filtrados)
        except:
            execucao = False
    
if __name__ == "__main__":
    main()