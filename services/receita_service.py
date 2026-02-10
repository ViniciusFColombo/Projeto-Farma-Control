from models.receita import Receita
from models.medico import Medico
from models.item_receita import ItemReceita
from repositories.receita_repo import buscar_receita_cliente_id
from services.cliente_service import Cliente
from services.item_receita_service import alterar_medicamentos_receita
from utils.filtros_pesquisas import listar_cliente_por_nome, listar_cliente_por_cpf
from utils.filtros_pesquisas import listar_medico_por_nome, listar_medico_por_crm
from utils.filtros_pesquisas import listar_medicamento_por_nome
from datetime import datetime
from database.connection import get_connection

def escolher_listagem_cliente():
    opcao = int(input("Deseja procurar por 1 - Nome ou 2 - CPF: "))
    if opcao == 1 :
        cliente = listar_cliente_por_nome()
    else :
        cliente = listar_cliente_por_cpf()
    return cliente

def escolher_listagem_medico():
    opcao = int(input("Deseja procurar por 1 - Nome ou 2 - CRM: "))
    if opcao == 1 :
        medico = listar_medico_por_nome()
    else :
        medico = listar_medico_por_crm()
    return medico

def cadastrar_receita():
    cliente = escolher_listagem_cliente()
    medico = escolher_listagem_medico()

    data_str = input("Data da receita (dd/mm/aaaa): ")
    data_receita = datetime.strptime(data_str, "%d/%m/%Y")
    data_ultima_retirada=None
    proxima_data=None
    status_vencida=False
    
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("""INSERT INTO receita (cliente_id, medico_id, data_receita, data_ultima_retirada, 
                   proxima_data_prevista, status)
                VALUES (?, ?, ?, ?, ?, ?)""")
    
    cursor.execute(comando_sql, (cliente.id, medico.id, data_receita, data_ultima_retirada, proxima_data, int(status_vencida)))
    conn.commit()
    receita_id = cursor.lastrowid

    itens = []

    while True:
        medicamento = listar_medicamento_por_nome()
        if not medicamento:
            continue

        quantidade = int(input("Quantidade: "))
        unidade = input("Unidade (comprimidos, frascos, etc): ")

        item = ItemReceita(
            receita=receita_id,
            medicamento=medicamento,
            quantidade=quantidade,
            unidade=unidade
        )

        itens.append(item)

        op = input("Adicionar outro medicamento? (s/n): ")
        if op.lower() == "n":
            break

    comando_item_sql = ("""INSERT INTO receita_medicamento (receita_id, medicamento_id, quantidade, unidade)
        VALUES (?, ?, ?, ?)""")

    for item in itens:
        cursor.execute(comando_item_sql, (receita_id, item.medicamento.id, item.quantidade, item.unidade))

    conn.commit()
    conn.close()

    print("Receita cadastrada com sucesso!")


def consultar_receita(cliente_id):
    rows = buscar_receita_cliente_id(cliente_id)

    if not rows:
        print("Nenhuma receita encontrada")
        return []

    receitas = []

    for row in rows:
        cliente = Cliente(
            id=row["cliente_id"],
            nome=row["cliente_nome"],
            cpf=row["cliente_cpf"],
            telefone=row["telefone"],
            status=bool(row["cliente_status"])
        )

        medico = Medico(
            id=row["medico_id"],
            nome=row["medico_nome"],
            crm=row["crm"]
        )

        receita = Receita(
            id=row["id"],
            cliente=cliente,
            medico=medico,
            data_receita=row["data_receita"],
            data_ultima_retirada=row["data_ultima_retirada"],
            proxima_data=row["proxima_data_prevista"],
            status_vencida=bool(row["status"]),
            itens=[]  # medicamentos entram depois
        )

        receitas.append(receita)

    return receitas



def alterar_receita(receita):
    conn = get_connection()
    cursor = conn.cursor()

    print("\n1 - Alterar Medico")
    print("2 - Alterar data da receita")
    print("3 - Alterar itens da receita")
    opcao = int(input("Escolha: "))

    match opcao:
        case 1:
            medico = escolher_listagem_medico()

            conn = get_connection()
            cursor = conn.cursor()

            comando_sql = ("""UPDATE receita SET medico_id = ? WHERE id = ?""")

            cursor.execute(comando_sql, (medico.id, receita.id))

            receita.medico = medico

        case 2:
            data_str = input("Data da receita (dd/mm/aaaa): ")
            data_receita = datetime.strptime(data_str, "%d/%m/%Y")

            conn = get_connection()
            cursor = conn.cursor()

            comando_sql = ("""UPDATE receita SET data_receita = ? WHERE id = ?""")

            cursor.execute(comando_sql, (data_receita, receita.id))
            
            receita.data_receita = data_receita

        case 3:
            itens = alterar_medicamentos_receita(receita, cursor)

    conn.commit()
    conn.close()

    print("Alterado com sucesso")
    return receita


def alterar_retirada(receita):
    data_str = input("Data da retirada (dd/mm/aaaa): ")
    nova_data = datetime.strptime(data_str, "%d/%m/%Y")

    receita.alterar_retirada(nova_data)

    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = """
        UPDATE receita
        SET data_ultima_retirada = ?, proxima_data_prevista = ?
        WHERE id = ?
    """

    cursor.execute(
        comando_sql,
        (
            receita.data_ultima_retirada,
            receita.proxima_data,
            receita.id
        )
    )

    conn.commit()
    conn.close()

    print("Retirada atualizada com sucesso.")