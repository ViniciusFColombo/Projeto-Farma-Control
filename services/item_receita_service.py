from repositories.item_receita_repo import consultar_medicamentos_por_receita_id
from utils.filtros_pesquisas import listar_medicamento_por_nome
from models.item_receita import ItemReceita
from models.medicamento import Medicamento
from database.connection import get_connection

def consultar_medicamentos_por_receita(receita):
    rows = consultar_medicamentos_por_receita_id(receita.id)

    if not rows:
        print("Nenhum medicamento encontrado")
        return []

    itens = []

    for row in rows:
        medicamento = Medicamento(
            id=row[0],
            nome=row[1],
            dosagem=row[2]
        )

        item = ItemReceita(
            receita=receita,
            medicamento=medicamento,
            quantidade=row[3],
            unidade=row[4]
        )

        itens.append(item)

    return itens

def alterar_medicamentos_receita(receita):
    while True:
        print("\n--- Medicamentos da Receita ---")
        itens = consultar_medicamentos_por_receita(receita)

        if not itens:
            print("Nenhum medicamento cadastrado")

        for i, item in enumerate(itens):
            print(f"{i + 1} - {item.medicamento.nome} | {item.quantidade} {item.unidade}")

        print("\n1 - Adicionar medicamento")
        print("2 - Remover medicamento")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_item_receita(receita)

        elif opcao == "2":
            remover_item_receita(receita, itens)

        elif opcao == "0":
            break

def adicionar_item_receita(receita, cursor):
    medicamento = listar_medicamento_por_nome()
    quantidade = int(input("Quantidade: "))
    unidade = input("Unidade: ")

    comando_sql = """
        INSERT INTO receita_medicamento (receita_id, medicamento_id, quantidade, unidade)
        VALUES (?, ?, ?, ?)
    """

    cursor.execute(
        comando_sql,
        (receita.id, medicamento.id, quantidade, unidade)
    )

def remover_item_receita(receita, itens, cursor):
    if not itens:
        print("Nenhum item para remover")
        return

    escolha = int(input("Escolha o item para remover: ")) - 1

    if escolha < 0 or escolha >= len(itens):
        print("Opção inválida")
        return

    item = itens[escolha]

    comando_sql = """
        DELETE FROM receita_medicamento
        WHERE receita_id = ? AND medicamento_id = ?
    """

    cursor.execute(comando_sql, (receita.id, item.medicamento.id))

