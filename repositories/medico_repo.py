from database.connection import get_connection
from models.medico import Medico

def inserir_medico(nome, crm):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("""INSERT INTO medico (nome, crm)
                   VALUES (?, ?)""")
    
    cursor.execute(comando_sql, (nome, crm))
    conn.commit()
    conn.close()

def atualizar_medico(novo_nome, novo_crm, medico):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("""UPDATE medico SET nome = ?, crm = ?
                       WHERE id = ?""")

    cursor.execute(comando_sql, (novo_nome, novo_crm, medico.id))
    conn.commit()
    conn.close()    

def buscar_medico_por_nome(nome):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("""SELECT id, nome, crm
                   FROM medico
                   WHERE nome LIKE ?""")
    
    cursor.execute(comando_sql, (f"%{nome}%",))
    rows = cursor.fetchall()

    conn.close()

    medicos =[]
    for row in rows:
        medico = Medico(
            id=row[0],
            nome=row[1],
            crm=row[2]
        )
        medicos.append(medico)
    return medicos

def buscar_medico_por_crm(crm):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("SELECT * FROM medico WHERE crm = ?")

    cursor.execute(comando_sql, (crm,))
    row = cursor.fetchone()

    conn.close()
   
    if not row:
        return None

    medico = Medico(
        id=row[0],
        nome=row[1],
        crm=row[2]
    )

    return medico