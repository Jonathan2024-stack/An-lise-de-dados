import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import time

# Função para buscar e analisar dados do Bitcoin
def analisar_bitcoin():
    # Baixar os dados mais recentes do Bitcoin
    btc_data = yf.download('BTC-USD', period='7d', interval='1m')  # Últimos 7 dias, com intervalo de 1 minuto

    # Verificar se os dados foram carregados
    if btc_data.empty:
        print("Não foi possível carregar os dados do Bitcoin. Verifique sua conexão com a internet.")
        return

    # Ajustar colunas multi-índice, se necessário
    btc_data.columns = [col[0] if isinstance(col, tuple) else col for col in btc_data.columns]

    if 'Close' in btc_data.columns:
        # Limpar os dados e converter para numéricos
        btc_data = btc_data[['Close']].dropna()
        btc_data['Close'] = btc_data['Close'].astype(float)

        # Calcular médias móveis
        btc_data['Média Curta (20 períodos)'] = btc_data['Close'].rolling(window=20).mean()
        btc_data['Média Longa (50 períodos)'] = btc_data['Close'].rolling(window=50).mean()

        # Sinal de compra/venda
        btc_data['Sinal'] = np.where(btc_data['Média Curta (20 períodos)'] > btc_data['Média Longa (50 períodos)'], 'Compra', 'Venda')

        # Última sugestão
        ultima_sugestao = 'Compra' if btc_data['Sinal'].iloc[-1] == 'Compra' else 'Venda'

        # Estatísticas básicas
        media = btc_data['Close'].mean()
        mediana = btc_data['Close'].median()
        desvio_padrao = btc_data['Close'].std()

        print("\n--- Análise em Tempo Real ---")
        print(f"Preço Atual: ${btc_data['Close'].iloc[-1]:.2f}")
        print(f"Média de preço: ${media:.2f}")
        print(f"Mediana de preço: ${mediana:.2f}")
        print(f"Desvio padrão (volatilidade): ${desvio_padrao:.2f}")
        print(f"Sugestão: {ultima_sugestao}")

        # Plotar o gráfico
        plt.figure(figsize=(14, 7))
        plt.plot(btc_data.index, btc_data['Close'], label='Preço de Fechamento', color='blue')
        plt.plot(btc_data.index, btc_data['Média Curta (20 períodos)'], label='Média Curta (20 períodos)', color='orange')
        plt.plot(btc_data.index, btc_data['Média Longa (50 períodos)'], label='Média Longa (50 períodos)', color='green')

        # Destaques de compra/venda
        compra = btc_data[btc_data['Sinal'] == 'Compra']
        venda = btc_data[btc_data['Sinal'] == 'Venda']
        plt.scatter(compra.index, compra['Close'], label='Sinal de Compra', marker='^', color='lime', alpha=1)
        plt.scatter(venda.index, venda['Close'], label='Sinal de Venda', marker='v', color='red', alpha=1)

        # Personalização do gráfico
        plt.title('Análise em Tempo Real do Bitcoin', fontsize=16)
        plt.xlabel('Data/Hora', fontsize=12)
        plt.ylabel('Preço de Fechamento (USD)', fontsize=12)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Exibir o gráfico
        plt.show()

    else:
        print("A coluna 'Close' não está disponível nos dados. Verifique o formato do DataFrame.")

# Loop para execução contínua
while True:
    analisar_bitcoin()
    time.sleep(60)  # Esperar 1 minuto antes de atualizar