def inspecionar_dados(dados):
    print("\nInformações dos dados:")
    dados.info()

def calcular_retornos(dados):
   
    retornos = dados.pct_change().dropna()
    return retornos
