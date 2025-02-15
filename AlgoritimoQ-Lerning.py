import random 
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime

# carregando dados 

df = pd.read_csv('dataset.csv')


# vamos trabalhar com a cotação de fechamneto das ações da Aplle
precos = df['AAPL.Close'].values


# Configuração do Algoritimo Q-Lerning

num_episodios = 1000 # numero de vezes que o algoritomo executará o procedimento
alfa = 0.1 # taxa de aprendizado do algoritimo, como ele vai levar em consideção novas informações.
gama = 0.99 # Fator de desconto, quanto ele vai valorizar. Recompeças futuras
epsilon = 0.1 # politica de exploração 

# Configurando o Ambiente de Negociação

print('\nConfiguração do Ambiente de Negociação..')
acoes = ['comprar', 'vender', 'manter']
saldo_inicial = 1000
num_acoes_inicial = 0

# Funções Para Executar as Ações (Passos) do Robô

# Função para executar uma ação e retornar a recompensa e o próximo estado
def executar_acao(estado, acao, saldo, num_acoes, preco):
    
    # Ação de comprar
    if acao == 0:
        if saldo >= preco:
            num_acoes += 1
            saldo -= preco
            
    # Ação de vender        
    elif acao == 1:
        if num_acoes > 0:
            num_acoes -= 1
            saldo += preco
            
    # Definição de çucro
    lucro = saldo + num_acoes * preco - saldo_inicial
    
    return (saldo, num_acoes, lucro)
            
# Treinamento do Robô

# Inicilizar a tabela Q
print('\nInicializando a tabela Q')
q_tabela = np.zeros((len(precos), len(acoes)))

# treinamento 
print('\nInicilaizando o Treinamento')
for _ in range(num_episodios):
    
    # Definir o Saldo
    saldo = saldo_inicial
    
    # Definir o numero de ações 
    num_acoes = num_acoes_inicial
    
    # Loop
    for i, preco in enumerate(precos[:-1]):
        estado = i
        
        if np.random.random() < epsilon:
            acai = random.choice(range(len(acoes)))
        else:
            acao = np.argmax(q_tabela[estado])
            
        # Executar a ação e obter a recompensa e o próximo estado
        saldo, num_acoes, lucro = executar_acao(estado, acao, saldo, num_acoes, preco)
        prox_estado = i + 1
        
        # ataualizar a tabela Q
        q_tabela[estado][acao] += alfa * (lucro + gama * np.max(q_tabela[prox_estado]) - q_tabela[estado][acao])
        
print('\nTreinamento Concluido...')

# Executando o Robô

# Valores iniciais para testar o agente 
saldo = saldo_inicial
num_acoes = num_acoes_inicial

print('\nExecutando o Agente...')
for i, preco in enumerate(precos[:-1]):
    estado = i
    acao = np.argmax(q_tabela[estado])
    saldo, num_acoes, _ = executar_acao(estado, acao, saldo, num_acoes, preco)
    
print('\nExecução concluída...')

# vendendo todas as ações no último preço
saldo += num_acoes * precos[-1]
lucro = saldo - saldo_inicial
lucro_final = round(lucro,2)

print(f'\nComeçamos a negociação com saldo inicial de 1000 e tívemos lucro de: {lucro_final}')