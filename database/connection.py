import sqlite3
import os

# raiz do projeto
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# caminho EXATO do banco
DB_PATH = os.path.join(PROJECT_ROOT, "data", "farma_control_TESTE.db")

def get_connection():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(
            f"Banco de dados não encontrado em: {DB_PATH}"
        )

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn



