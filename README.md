
Este projeto tem como objetivo coletar, processar e analisar dados históricos de ações brasileiras, aplicando conceitos de análise de dados e engenharia de dados em um pipeline estruturado.

Foram utilizadas as seguintes ferramentas

* Python
* Pandas
* Matplotlib
* SQLite
* yfinance

O projeto foi organizado seguindo um modelo de pipeline ETL (Extract, Transform, Load):

```bash
analise-acoes/
│
├── data/               # Dados gerados (CSV e banco SQLite)
│   ├── precos_acoes.csv
│   ├── retornos_acoes.csv
│   └── acoes.db
│
├── src/
│   ├── extract.py      # Coleta de dados
│   ├── transform.py    # Tratamento e cálculo de métricas
│   ├── load.py         # Persistência em banco de dados
│   ├── queries.py      # Consultas SQL
│   └── main.py         # Orquestração do pipeline
│
├── graficos-dashboard/
│   ├── acoes.pbix
│   ├── acoes.png
│   ├── matplot_acoes.png
│   ├── matplot_retorno.png
│   └── matplot_retorno_carteira.png
│
├── README.md
└── requirements.txt
```


Os dados são coletados utilizando a biblioteca `yfinance`, com foco no preço de fechamento das ações.


* Houve a inspeção dos dados(`.info()`)
* Cálculo de retornos percentuais (`pct_change`)
* Tratamento de valores nulos gerados na transformação


Os dados são armazenados em:

* Arquivos CSV (para análise externa)
* Banco de dados SQLite (para consultas SQL)

As seguinte análises foram realizadas:

### Retorno Médio

Mede o desempenho médio diário de cada ativo.

### Volatilidade

Representa o risco, baseado na variação dos retornos.

###  Correlação

Avalia o grau de relação entre os ativos, importante para diversificação.

Após os resultados, o projeto gera gráficos para:

* Evolução do preço das ações (matplot_acoes.png)
* Retorno acumulado (matplot_retorno.png)
* Desempenho de uma carteira simulada  (matplot_retorno_carteira.png)



Foi construída uma carteira simples com pesos fixos entre os ativos, permitindo avaliar o comportamento conjunto dos investimentos ao longo do tempo.


Os dados são armazenados em um banco SQLite (`acoes.db`) e consultados via SQL diretamente no Python.

Exemplo de consulta:

```sql
SELECT *
FROM retornos
WHERE "PETR4.SA" > 0.02
```



##  Resultados Obtidos



* Total de registros: 1575
* Nenhum valor nulo identificado
* Dados numéricos consistentes (float64)



###  Retorno Médio Diário

```
ITUB4.SA    0.000578
PETR4.SA    0.001448
VALE3.SA    0.000874
```

A PETR4 apresentou o maior retorno médio, enquanto ITUB4 mostrou comportamento mais conservador.

---

###  Volatilidade (Risco)

```
ITUB4.SA    0.019104
PETR4.SA    0.025990
VALE3.SA    0.022218
```

PETR4 é o ativo mais volátil (maior risco), enquanto ITUB4 é o mais estável.



###  Correlação

```
          ITUB4.SA  PETR4.SA  VALE3.SA
ITUB4.SA  1.000000  0.469548  0.363691
PETR4.SA  0.469548  1.000000  0.437772
VALE3.SA  0.363691  0.437772  1.000000
```

Os ativos apresentam correlação moderada, indicando diversificação parcial.

---

### 🔍 Consulta SQL – Altos Retornos

```
Date         PETR4.SA
2020-01-28   0.027470
2020-02-06   0.027827
2020-02-12   0.022049
2020-02-19   0.026891
2020-03-02   0.046961
```
A Petrobras teve dias fortes de crescimentos no primeiro trimestre de 2020, mas ao se analisar os gráficos se percebe que também houve fortes quedas. Concluindo que esses crescimentos foram resultados de recuperação de quedas/volatilidade no mercado (possivelmente causados pela pandemia de COVID-19 na época).


##  Principais Insights

* PETR4 apresenta maior retorno e maior risco
* ITUB4 é mais estável e conservadora
* VALE3 possui comportamento intermediário
* A diversificação entre os ativos é limitada


Para maior interação, foi criado um dashboard simples contendo o retorno médio diário, volatilidade média e total de ativos analisados, além dos gráficos de valores e retornos médios com filtros por período de tempo. Dashboard este disponível em acoes.pbix ou no print acoes.png se apenas quiser ver.
##  Como Executar

1. Clone o repositório

```bash
git clone https://github.com/vitorvieira2288/Analise_Bolsa_Brasileira.git
cd analise-acoes
```

2. Instale as dependências

```bash
pip install -r requirements.txt
```

3. Execute o projeto

```bash
python -m src.main
```



