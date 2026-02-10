from database.connection import get_connection

medicos = []

def buscar_medico_por_id(id):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("SELECT * FROM medico WHERE id = ?")
    
    cursor.execute(comando_sql, (id,))
    row = cursor.fetchone()

    conn.close()
    return row

def buscar_medico_por_nome(nome):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("""SELECT id, nome, crm
                   FROM medico
                   WHERE nome LIKE ?""")
    
    cursor.execute(comando_sql, (f"%{nome}%",))
    rows = cursor.fetchall()

    conn.close()
    return rows

def buscar_medico_por_crm(crm):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("SELECT * FROM medico WHERE crm = ?")

    cursor.execute(comando_sql, (crm,))
    row = cursor.fetchone()

    conn.close()
    return row