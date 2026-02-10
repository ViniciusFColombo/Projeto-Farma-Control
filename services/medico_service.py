from models.medico import Medico
from repositories.medico_repo import buscar_medico_por_id
from database.connection import get_connection
from utils.formatacao import padronizar_nome, somente_numeros
from utils.filtros_pesquisas import listar_medico_por_crm, listar_medico_por_nome

def escolher_listagem_medico():
    opcao = int(input("Deseja procurar por 1 - Nome ou 2 - CRM: "))
    if opcao == 1 :
        medico = listar_medico_por_nome()
    else :
        medico = listar_medico_por_crm()
    return medico

def cadastrar_medico():
    nome = padronizar_nome(input("Nome do médico: "))
    crm = somente_numeros(input("CRM: "))

    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("""INSERT INTO medico (nome, crm)
                   VALUES (?, ?)""")
    
    cursor.execute(comando_sql, (nome, crm))
    conn.commit()
    conn.close()

    print("Médico cadastrado com sucesso!")

def consultar_medico():
    medico = escolher_listagem_medico()

    print(f"Nome: {medico.nome} | CRM: {medico.crm}")
    return medico

def alterar_medico():
    medico = consultar_medico()

    if medico:
        novo_nome = padronizar_nome(input("Novo nome: "))
        novo_crm = somente_numeros(input("Novo CRM: "))

        conn = get_connection()
        cursor = conn.cursor()

        comando_sql = ("""UPDATE medico SET nome = ?, crm = ?
                       WHERE id = ?""")

        cursor.execute(comando_sql, (novo_nome, novo_crm, medico.id))
        conn.commit()
        conn.close()
        print("Dados alterados com sucesso!")