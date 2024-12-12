import pandas as pd

# função para criar uma linha para separação dos blocos de códigos executados.
def lin():
    return print('=-=-'  * 14)

# Vizualisando os dados
df = pd.read_csv("/storage/emulated/0/análise_de_dados/produtos.csv")
    
    # trabalhando com dados da coluna 'custo'
    # Nesse caso fazendo a soma dos valores.
custo_de_produtos = df['custo'].sum()
    
    # Trabalhando com dados da coluna 'preco_unitario'
    # Neste caso exibindo tanbém a soma dos valores.
preço_de_venda = round(df['preco_unitario'].sum(),2)
    
    # Obtendo o valor do lucro esperado pela enpresa.
lucro_esperado = (preço_de_venda - custo_de_produtos)
   
   # Criando Menu de opções
lin() 
print('ANÁLISE DE PRODUTOS EM ESTOQUE')
lin()
print('''Escolha uma opção abaixo para saber a respeito de cada ponto ecpecifíco:\n
    [1] Valor total que a Enpresa investiu em produtos
    [2] Valor total sugeridos pela enpresa já no valor de venda
    [3] Valor do lucro  experado pela enpresa \n
    Ou se desejá ver o resumo da análise didite [4]\n
    Para sair [5].''')
lin()   
    # Criando laço de repetição do menu e botão de sair. 
while True:
    msg = int(input('Opção desejada : '))
    lin()
    if msg == 1:
        print(f'''[1] Valor total que a Enpresa investiu em produtos:
        O valor investido em produtos é de R$ ({custo_de_produtos})''')
    elif msg == 2:
        print(f'''[2] Valor total sugeridos pela enpresa já no valor de venda:
O valor total pelo qual os produtos seram vendidos estimula se em 
R$ ({preço_de_venda})''')
    elif msg == 3:
        print(f'''[3] Valor do lucro  experado pela enpresa:
        o Valor total em lucros esperados é de 
    R$ ({lucro_esperado}).''')
    elif msg == 4:
        print(f'''[4] resumo da análise:
        O valor investido em produtos é de R$ ({custo_de_produtos}), \nE o valor total pelo qual os produtos seram vendidos estimula se em 
    R$ ({preço_de_venda}), portanto o Valor total em lucros esperados é de 
    R$ ({lucro_esperado}).''')
    else:
        print('até logo...')
        break
    lin()
