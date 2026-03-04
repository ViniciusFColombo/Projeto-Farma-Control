from database.connection import get_connection

def inserir_receita_na_lista(lista_id, receitas, status):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = """
            INSERT INTO lista_receita (lista_id, receita_id, status)
            VALUES (?, ?, ?)
        """

        for receita_id in receitas:
            cursor.execute(comando_sql, (lista_id, receita_id, status))

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def atualizar_status(lista_id, receita_id, status):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = """
        UPDATE lista_receita
        SET status = ?
        WHERE lista_id = ?
        AND receita_id = ?
        """

        cursor.execute(comando_sql, (status, lista_id, receita_id))

        # opcional mas MUITO recomendado:
        if cursor.rowcount == 0:
            raise Exception("Registro não encontrado para atualização.")

        conn.commit()

    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def buscar_clientes_nao_marcados(lista_id):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = """
    SELECT DISTINCT c.id, c.nome, c.cpf
    FROM lista_receita lr
    JOIN receita r ON r.id = lr.receita_id
    JOIN cliente c ON c.id = r.cliente_id
    WHERE lr.lista_id = ?
    AND lr.status = ?
    """

    cursor.execute(comando_sql, (lista_id, "PENDENTE"))
    resultados = cursor.fetchall()

    conn.close()
    return resultados  

def buscar_receitas_completas_da_lista(lista_id):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = """
        SELECT
            r.id,
            r.data_receita,
            c.nome,
            c.cpf,
            m.nome,
            m.crm
        FROM lista_receita lr
        JOIN receita r ON r.id = lr.receita_id
        JOIN cliente c ON c.id = r.cliente_id
        JOIN medico m ON m.id = r.medico_id
        WHERE lr.lista_id = ?
    """

    cursor.execute(comando_sql, (lista_id,))
    rows = cursor.fetchall()
    conn.close()

    return rows

    
    
