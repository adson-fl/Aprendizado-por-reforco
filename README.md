# Algoritmo de Aprendizado por Reforço para Negociação de Ações 📈

Este projeto foi desenvolvido em aula durante o curso **Fundamentos de Linguagem Python para Análise de Dados e Data Science** da **Data Science Academy**. Ele implementa um **algoritmo de Aprendizado por Reforço (Q-Learning)** para simular negociações de ações da Apple (AAPL) com base em dados históricos.

## 📌 Funcionalidades
- Carregamento de dados históricos de ações.
- Implementação do algoritmo **Q-Learning**.
- Simulação de compra e venda de ações.
- Cálculo do lucro baseado na estratégia aprendida.
- Visualização dos resultados.

## 📂 Estrutura do Projeto
```
📁 projeto-qlearning
│-- dataset.csv  # Arquivo com os dados das ações da AAPL
│-- main.py       # Código principal do algoritmo
│-- README.md     # Este arquivo de documentação
│-- .gitignore    # Arquivo para ignorar arquivos desnecessários
```

## 🚀 Como Executar
1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/projeto-qlearning.git
   cd projeto-qlearning
   ```
2. **Instale as dependências**
   ```bash
   pip install numpy pandas plotly
   ```
3. **Execute o código**
   ```bash
   python main.py
   ```

## 📊 Bibliotecas Utilizadas
- `numpy`: Operações matemáticas e manipulação de arrays.
- `pandas`: Leitura e manipulação de dados.
- `plotly`: Visualização dos resultados.
- `random`: Exploração de ações dentro do aprendizado por reforço.

## 📌 Explicação do Algoritmo
O **Q-Learning** é um algoritmo de aprendizado por reforço baseado em uma **tabela Q**, que armazena valores de recompensa para diferentes estados e ações. O modelo aprende iterativamente a melhor estratégia de negociação por meio da exploração e atualização da tabela Q.

Parâmetros principais:
- `num_episodios = 1000` → Número de iterações de treinamento.
- `alfa = 0.1` → Taxa de aprendizado.
- `gama = 0.99` → Fator de desconto para recompensas futuras.
- `epsilon = 0.1` → Probabilidade de exploração.

## 📌 Resultados
Ao final da execução, o código exibe o lucro obtido após a simulação das negociações baseadas no aprendizado do robô.

---
✍️ *Projeto criado para aprendizado e experimentação com aprendizado por reforço!* 🚀
