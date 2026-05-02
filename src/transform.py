def inspecionar_dados(dados):
    print("\nInformações dos dados:")
    dados.info()

def calcular_retornos(dados):
    # pct_change gera NaN na primeira linha → removemos
    retornos = dados.pct_change().dropna()
    return retornos