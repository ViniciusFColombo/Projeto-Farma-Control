from database.connection import get_connection
from models.medicamento import Medicamento
from models.item_receita import ItemReceita


def consultar_medicamentos_por_receita_id(receita_id):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = """
        SELECT 
            m.id,
            m.nome,
            m.dosagem,
            rm.quantidade,
            rm.unidade
            FROM receita_medicamento rm
            JOIN medicamento m ON m.id = rm.medicamento_id
            WHERE rm.receita_id = ?
            ORDER BY m.nome
         """

    cursor.execute(comando_sql, (receita_id,))
    rows = cursor.fetchall()
    conn.close()

    lista_itens = []

    for row in rows:
        medicamento = Medicamento(
            id=row[0],
            nome=row[1],
            dosagem=row[2]
        )

        item = ItemReceita(
            receita=receita_id,
            medicamento=medicamento,
            quantidade=row[3],
            unidade=row[4]
        )

        lista_itens.append(item)

    return lista_itens

def adicionar_item_receita(receita_id, medicamento_id, quantidade, unidade):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = """
            INSERT INTO receita_medicamento (receita_id, medicamento_id, quantidade, unidade)
            VALUES (?, ?, ?, ?)
        """

        cursor.execute(
            comando_sql,
            (receita_id, medicamento_id, quantidade, unidade)
        )

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def apagar_item_receita(receita_id, medicamento_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = """
            DELETE FROM receita_medicamento
            WHERE receita_id = ? AND medicamento_id = ?
        """

        cursor.execute(comando_sql, (receita_id, medicamento_id))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


