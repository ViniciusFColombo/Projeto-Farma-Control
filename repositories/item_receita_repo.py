from database.connection import get_connection


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

    return rows

