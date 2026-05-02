import sqlite3

def salvar_no_banco(dados, retornos, caminho_banco="data/acoes.db"):
    conn = sqlite3.connect(caminho_banco)

    dados.to_sql("precos", conn, if_exists="replace")
    retornos.to_sql("retornos", conn, if_exists="replace")

    conn.close()