import sqlite3
import pandas as pd

def buscar_altos_retornos(caminho_banco="data/acoes.db"):
    conn = sqlite3.connect(caminho_banco)

    query = """
    SELECT *
    FROM retornos
    WHERE "PETR4.SA" > 0.02
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df


def calcular_correlacao(caminho_banco="data/acoes.db"):
    conn = sqlite3.connect(caminho_banco)

    df = pd.read_sql("SELECT * FROM retornos", conn)
    conn.close()

    return df.drop(columns=["Date"]).corr()