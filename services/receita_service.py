from models.receita import Receita
from models.item_receita import ItemReceita
from repositories.receita_repo import receitas, buscar_receita_por_id
from repositories.cliente_repo import buscar_cliente_por_id
from repositories.medico_repo import buscar_medico_por_id
from datetime import datetime, timedelta


def cadastrar_receita():
    id = len(receitas) + 1

    cliente_id = int(input("ID do cliente: "))
    cliente = buscar_cliente_por_id(cliente_id)
    if not cliente:
        print("Cliente não encontrado.")
        return

    medico_id = int(input("ID do médico: "))
    medico = buscar_medico_por_id(medico_id)
    if not medico:
        print("Médico não encontrado.")
        return

    data_str = input("Data da receita (dd/mm/aaaa): ")
    data_receita = datetime.strptime(data_str, "%d/%m/%Y")

    itens = []
    while True:
        nome = input("Medicamento: ")
        dosagem = input("Dosagem: ")
        quantidade = input("Quantidade: ")
        unidade = input("Unidade: ")

        item = ItemReceita(nome, dosagem, quantidade, unidade)
        itens.append(item)

        op = input("Adicionar outro item? (s/n): ")
        if op.lower() == "n":
            break

    receita = Receita(
        id=id,
        cliente=cliente,
        medico=medico,
        data_receita=data_receita,
        data_ultima_retirada=None,
        proxima_data=None,
        status_vencida=False,
        itens=itens
    )

    receita.verificar_vencimento()
    receitas.append(receita)

    print("Receita cadastrada com sucesso.")


def consultar_receita():
    id = int(input("ID da receita: "))
    receita = buscar_receita_por_id(id)

    if not receita:
        print("Receita não encontrada.")
        return None

    print("\n--- RECEITA ---")
    print(f"Cliente: {receita.cliente.nome}")
    print(f"Médico: {receita.medico.nome} | CRM: {receita.medico.crm}")
    print(f"Data da receita: {receita.data_receita.strftime('%d/%m/%Y')}")
    print(f"Vencida: {receita.status_vencida}")

    print("\nItens:")
    for item in receita.itens:
        print(f"- {item.nome} | {item.dosagem} | {item.quantidade} | {item.unidade}")

    return receita

def alterar_receita():
    receita = consultar_receita()
    if not receita:
        return

    print("\n1 - Registrar retirada")
    print("2 - Adicionar item")
    opcao = input("Escolha: ")

    if opcao == "1":
        receita.registrar_retirada()
        print("Retirada registrada.")

    elif opcao == "2":
        nome = input("Medicamento: ")
        dosagem = input("Dosagem: ")
        quantidade = input("Quantidade: ")

        item = ItemReceita(nome, dosagem, quantidade)
        receita.itens.append(item)

        print("Item adicionado com sucesso.")