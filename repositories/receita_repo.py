from database.connection import get_connection

def buscar_receita_cliente_id(cliente_id):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = """
        SELECT
            r.id,
            r.data_receita,
            r.data_ultima_retirada,
            r.proxima_data_prevista,
            r.status,
            
            c.id AS cliente_id,
            c.nome AS cliente_nome,
            c.cpf AS cliente_cpf,
            c.telefone,
            c.status AS cliente_status,

            m.id AS medico_id,
            m.nome AS medico_nome,
            m.crm

        FROM receita r
        JOIN cliente c ON c.id = r.cliente_id
        JOIN medico m ON m.id = r.medico_id

        WHERE r.cliente_id = ?
        ORDER BY r.data_receita DESC
        LIMIT 3
    """

    cursor.execute(comando_sql, (cliente_id,))
    rows = cursor.fetchall()
    conn.close()

    return rows
