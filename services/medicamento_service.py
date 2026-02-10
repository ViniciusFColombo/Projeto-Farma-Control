from models.medicamento import Medicamento
from repositories.medicamento_repo import buscar_medicamento_por_id
from utils.filtros_pesquisas import listar_medicamento_por_nome
from database.connection import get_connection
from utils.formatacao import padronizar_nome

def cadastrar_medicamento():
    nome = padronizar_nome(input("Nome do medicamento: "))
    dosagem = input("Dosagem do medicamento: ")
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("""INSERT INTO medicamento (nome, dosagem)
                   VALUES (?, ?)""")
    
    cursor.execute(comando_sql, (nome, dosagem))
    conn.commit()
    conn.close()
    print("Medicamento cadastrado com sucesso")


def consultar_medicamento():
    medicamento = listar_medicamento_por_nome()

    return medicamento
    

def alterar_medicamento():
    medicamento = consultar_medicamento()

    if medicamento:
        novo_nome = padronizar_nome(input("Novo nome: "))
        nova_dosagem = input("Nova dosagem: ")

        conn = get_connection()
        cursor = conn.cursor()

        comando_sql = ("""UPDATE medicamento SET nome = ?, dosagem = ?
                       WHERE id = ?""")

        cursor.execute(comando_sql, (novo_nome, nova_dosagem, medicamento.id))
        conn.commit()
        conn.close()
        print("Medicamento alterado com sucesso!")
