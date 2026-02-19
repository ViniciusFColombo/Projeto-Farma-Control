from services.receita_service import cadastrar_receita
from services.cliente_service import buscar_cliente_por_nome, buscar_cliente_por_cpf
from services.medico_service import buscar_medico_por_nome, buscar_medico_por_crm
from services.medicamento_service import buscar_medicamento_por_nome
from utils.formatacao import padronizar_nome, somente_numeros
from datetime import datetime
from models.item_receita import ItemReceita

def nova_receita():
    cliente = escolher_cliente()
    if not cliente:
        print("Cliente não encontrado.")
        return

    medico = escolher_medico()
    if not medico:
        print("Médico não encontrado.")
        return

    data_str = input("Data da receita (dd/mm/aaaa): ")
    data_receita = datetime.strptime(data_str, "%d/%m/%Y")

    itens = []

    while True:
        nome = input("Informe o nome do medicamento: ")
        medicamentos = buscar_medicamento_por_nome(nome)

        if not medicamentos:
            print("Medicamento não encontrado.")
            continue 

        if len(medicamentos) == 1:
            medicamento = medicamentos[0]
        else:
            print("\nMedicamentos encontrados:")
            for i, med in enumerate(medicamentos, start=1):
                print(f"{i} - {med.nome} {med.dosagem}")

            escolha = int(input("Escolha o medicamento: "))
            medicamento = medicamentos[escolha - 1]

        quantidade = int(input("Quantidade: "))
        unidade = input("Unidade: ")

        item = ItemReceita(
            receita=None,
            medicamento=medicamento,
            quantidade=quantidade,
            unidade=unidade
        )

        itens.append(item)

        op = input("Adicionar outro medicamento? (s/n): ")
        if op.lower() == "n":
            break

    if not itens:
        print("Nenhum medicamento foi adicionado.")
        return

    cadastrar_receita(cliente, medico, data_receita, itens)
    print("Receita cadastrada com sucesso!")


def escolher_cliente():
    opcao = int(input("Buscar por 1 - Nome ou 2 - CPF: "))

    if opcao == 1:
        nome = padronizar_nome(input("Nome: "))
        clientes = buscar_cliente_por_nome(nome)

        if not clientes:
            return None

        if len(clientes) == 1:
            return clientes[0]

        print("\nClientes encontrados:")
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i} - {cliente.nome} | CPF: {cliente.cpf}")

        escolha = int(input("Escolha o cliente: "))
        return clientes[escolha - 1]

    else:
        cpf = somente_numeros(input("CPF: "))
        return buscar_cliente_por_cpf(cpf)


def escolher_medico():
    opcao = int(input("Buscar por 1 - Nome ou 2 - CRM: "))

    if opcao == 1:
        nome = padronizar_nome(input("Nome: "))
        medicos = buscar_medico_por_nome(nome)

        if not medicos:
            return None

        if len(medicos) == 1:
            return medicos[0]

        print("\nMedicos encontrados:")
        for i, medico in enumerate(medicos, start=1):
            print(f"{i} - {medico.nome} | CRM: {medico.crm}")

        escolha = int(input("Escolha o medico: "))
        return medicos[escolha - 1]

    else:
        crm = somente_numeros(input("CRM: "))
        return buscar_medico_por_crm(crm)