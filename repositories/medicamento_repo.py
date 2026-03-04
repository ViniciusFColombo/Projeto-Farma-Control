from database.connection import get_connection
from models.medicamento import Medicamento

def inserir_medicamento(nome, dosagem):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = ("""INSERT INTO medicamento (nome, dosagem)
                    VALUES (?, ?)""")
        
        cursor.execute(comando_sql, (nome, dosagem))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def atualizar_medicamento(novo_nome, nova_dosagem, medicamento):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = ("""UPDATE medicamento SET nome = ?, dosagem = ?
                        WHERE id = ?""")

        cursor.execute(comando_sql, (novo_nome, nova_dosagem, medicamento.id))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def buscar_medicamento_por_nome(nome):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("""SELECT id, nome, dosagem
                   FROM medicamento
                   WHERE nome LIKE ?""")
    
    cursor.execute(comando_sql, (f"%{nome}%",))
    rows = cursor.fetchall()

    conn.close()
    medicamentos = []
    for row in rows:
        medicamento = Medicamento(
            id=row[0],
            nome=row[1],
            dosagem=row[2],
        )
        medicamentos.append(medicamento)
    return medicamentos
