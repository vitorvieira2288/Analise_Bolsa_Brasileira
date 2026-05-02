import os
import matplotlib.pyplot as plt

from src.extract import obter_dados
from src.transform import inspecionar_dados, calcular_retornos
from src.load import salvar_no_banco
from src.queries import buscar_altos_retornos, calcular_correlacao


def executar_pipeline():
    tickers = ["PETR4.SA", "VALE3.SA", "ITUB4.SA"]

    
    dados = obter_dados(tickers)

    
    inspecionar_dados(dados)

    
    retornos = calcular_retornos(dados)

    
    os.makedirs("data", exist_ok=True)

   
    dados.to_csv("data/precos_acoes.csv")
    retornos.to_csv("data/retornos_acoes.csv")

  
    salvar_no_banco(dados, retornos)

   
    
    print("\nRetorno médio:")
    print(retornos.mean())

    print("\nVolatilidade:")
    print(retornos.std())

    print("\nCorrelação:")
    print(retornos.corr())

  
    dados.plot(title="Preço das Ações", figsize=(10,5))
    plt.show()

    retornos.cumsum().plot(title="Retorno Acumulado", figsize=(10,5))
    plt.show()

   
    pesos = [0.33, 0.33, 0.34]
    carteira = (retornos * pesos).sum(axis=1)
    carteira.name = "Carteira"

    carteira.cumsum().plot(title="Retorno da Carteira", figsize=(10,5))
    plt.show()

    
    print("\nDias com alto retorno da PETR4:")
    print(buscar_altos_retornos().head())

    print("\nCorrelação via SQL:")
    print(calcular_correlacao())


if __name__ == "__main__":
    executar_pipeline()
