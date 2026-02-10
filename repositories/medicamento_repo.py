from database.connection import get_connection

def buscar_medicamento_por_id(id):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("SELECT * FROM medicamento WHERE id = ?")

    cursor.execute(comando_sql, (id,))
    row = cursor.fetchone()
    
    conn.close()
    return row

def buscar_medicamento_por_nome(nome):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("""SELECT id, nome, dosagem
                   FROM medicamento
                   WHERE nome LIKE ?""")
    
    cursor.execute(comando_sql, (f"%{nome}%",))
    rows = cursor.fetchall()

    conn.close()
    return rows