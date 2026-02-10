from database.connection import get_connection
clientes = []

def buscar_cliente_por_id(id):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("SELECT * FROM cliente WHERE id = ?")

    cursor.execute(comando_sql, (id,))
    row = cursor.fetchone()

    conn.close()

    return row

def buscar_cliente_por_nome(nome):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("""SELECT id, nome, cpf, telefone, status
                   FROM cliente
                   WHERE nome LIKE ?""")
    
    cursor.execute(comando_sql, (f"%{nome}%",))
    rows = cursor.fetchall()

    conn.close()
    return rows

def buscar_cliente_por_cpf(cpf):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("SELECT * FROM cliente WHERE cpf = ?")

    cursor.execute(comando_sql, (cpf,))
    row = cursor.fetchone()

    conn.close()

    return row