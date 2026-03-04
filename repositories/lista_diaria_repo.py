from database.connection import get_connection
from models.lista_diaria import ListaDiaria
from datetime import datetime


def criar_lista(data, status):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = "INSERT INTO lista_diaria (data_lista, status) VALUES (?, ?)"

        cursor.execute(comando_sql, (data.strftime("%Y-%m-%d"), status))
        conn.commit()
        lista_diaria_id = cursor.lastrowid
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    return lista_diaria_id


def atualizar_status_lista(id, status):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = "UPDATE lista_diaria SET status = ? WHERE id = ?"
        cursor.execute(comando_sql, (status, id))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def buscar_lista(data):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = "SELECT id, data_lista, status FROM lista_diaria WHERE data_lista = ?"

    cursor.execute(comando_sql, (data.strftime("%Y-%m-%d"),))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    lista_diaria = ListaDiaria(
        id=row[0],
        data_lista=datetime.strptime(row[1], "%Y-%m-%d").date(),
        status=row[2]
    )

    return lista_diaria

def excluir_lista(lista_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = "DELETE FROM lista_diaria WHERE id = ?"
        cursor.execute(comando_sql, (lista_id,))

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()