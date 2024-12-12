import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# Baixar dados históricos do Bitcoin (BTC-USD)
btc_data = yf.download('BTC-USD', start='2023-01-01', end='2023-12-31')

# Verificar se os dados foram carregados
if btc_data.empty:
    print("Não foi possível carregar os dados do Bitcoin. Verifique sua conexão com a internet.")
else:
    # Verificar a estrutura do DataFrame
    print("Estrutura dos dados carregados:")
    print(btc_data.info())

    # Ajustar colunas multi-índice
    btc_data.columns = [col[0] for col in btc_data.columns]  # Pegar apenas o primeiro nível do índice

    # Garantir que 'Close' exista no DataFrame
    if 'Close' in btc_data.columns:
        # Limpar os dados e converter para numéricos
        btc_data = btc_data[['Close']].dropna()
        btc_data['Close'] = btc_data['Close'].astype(float)

        # Calcular médias móveis
        btc_data['Média Curta (20 dias)'] = btc_data['Close'].rolling(window=20).mean()
        btc_data['Média Longa (50 dias)'] = btc_data['Close'].rolling(window=50).mean()

        # Sinal de compra/venda
        btc_data['Sinal'] = np.where(btc_data['Média Curta (20 dias)'] > btc_data['Média Longa (50 dias)'], 'Compra', 'Venda')

        # Estatísticas básicas
        media = btc_data['Close'].mean()
        mediana = btc_data['Close'].median()
        desvio_padrao = btc_data['Close'].std()

        print("Análise Estatística do Bitcoin:")
        print(f"Média de preço: ${media:.2f}")
        print(f"Mediana de preço: ${mediana:.2f}")
        print(f"Desvio padrão (volatilidade): ${desvio_padrao:.2f}")
        print("Estratégia de tomada de decisão baseada em médias móveis:")
        print(f"Sugestão final: {'Compra' if btc_data['Sinal'].iloc[-1] == 'Compra' else 'Venda'}")

        # Gráfico detalhado
        plt.figure(figsize=(14, 7))
        plt.plot(btc_data.index, btc_data['Close'], label='Preço de Fechamento', color='blue')
        plt.plot(btc_data.index, btc_data['Média Curta (20 dias)'], label='Média Curta (20 dias)', color='orange')
        plt.plot(btc_data.index, btc_data['Média Longa (50 dias)'], label='Média Longa (50 dias)', color='green')

        # Destaques de compra/venda
        compra = btc_data[btc_data['Sinal'] == 'Compra']
        venda = btc_data[btc_data['Sinal'] == 'Venda']
        plt.scatter(compra.index, compra['Close'], label='Sinal de Compra', marker='^', color='lime', alpha=1)
        plt.scatter(venda.index, venda['Close'], label='Sinal de Venda', marker='v', color='red', alpha=1)

        # Personalização do gráfico
        plt.title('Análise do Bitcoin com Estratégia de Tomada de Decisão', fontsize=16)
        plt.xlabel('Data', fontsize=12)
        plt.ylabel('Preço de Fechamento (USD)', fontsize=12)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Exibir o gráfico
        plt.show()
    else:
        print("A coluna 'Close' não está disponível nos dados. Verifique o formato do DataFrame.")