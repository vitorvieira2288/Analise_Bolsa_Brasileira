import yfinance as yf

def obter_dados(tickers, data_inicio="2020-01-01"):
    dados = yf.download(tickers, start=data_inicio)["Close"]
    return dados