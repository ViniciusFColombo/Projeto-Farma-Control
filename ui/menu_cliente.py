from services.cliente_service import cadastrar_cliente, buscar_cliente_por_nome, buscar_cliente_por_cpf, alterar_cliente, buscar_receitas_cliente
from utils.formatacao import padronizar_nome, somente_numeros
from ui import menu_receita


def menu_cliente():
    while True:
        print("\n--- MENU CLIENTE ---")
        print("1 - Cadastrar cliente")
        print("2 - Consultar cliente")
        print("3 - Alterar cliente")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        match opcao:
            case "1":
                nome = padronizar_nome(input("Nome do cliente: "))
                cpf = somente_numeros(input("CPF do cliente: "))
                telefone = somente_numeros(input("Telefone do cliente: "))

                cadastrar_cliente(nome, cpf, telefone)
                print("Cliente cadastrado com sucesso!")

            case "2":
                cliente = escolher_cliente()

                if not cliente:
                    print("Cliente não encontrado.")
                    continue
                
                cliente_id = cliente.id
                menu_receita(cliente_id)

            case "3":
                cliente = escolher_cliente()
                if not cliente:
                    print("Cliente não encontrado.")
                    continue

                novo_nome = padronizar_nome(input("Novo nome: "))
                novo_cpf = somente_numeros(input("Novo CPF: "))
                novo_telefone = somente_numeros(input("Novo telefone: "))
                status_input = int(input("0 - Desativar | 1 - Ativar: "))

                novo_status = True if status_input == 1 else False

                alterar_cliente(cliente.id, novo_nome, novo_cpf, novo_telefone, novo_status)
                print("Cliente atualizado com sucesso!")

            case "0":
                return

            case _:
                print("Opção inválida.")


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

    elif opcao == 2:
        cpf = somente_numeros(input("CPF: "))
        return buscar_cliente_por_cpf(cpf)

    else:
        print("Opçao invalida")
        return
