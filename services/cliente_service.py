from models.cliente import Cliente
from repositories.cliente_repo import clientes

def cadastrar_cliente():
    id = len(clientes) + 1
    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    telefone = input("Telefone do cliente: ")
    status = True

    cliente = Cliente(id, nome, cpf, telefone, status)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def consultar_cliente():
    id = int(input("Insira o ID do cliente: "))
    for cliente in clientes:
        if cliente.id == id:
            print(f"ID: {cliente.id}")
            print(f"Nome: {cliente.nome}")
            print(f"CPF: {cliente.cpf}")
            print(f"Telefone: {cliente.telefone}")
            print(f"Status: {cliente.status}")
            return cliente
    print("Cliente não encontrado")
    return None

def alterar_cliente():
    cliente = consultar_cliente()

    if cliente:
        novo_nome = input("Novo nome: ")
        novo_cpf = input("Novo CPF:" )
        novo_telefone = input("Novo telefone: ")
        opcao = int(input("Novo status (0 - ""Desativar""/ 1 - ""Ativar""):"))
        novo_status = True
        if opcao == 0:
            novo_status = False
        else:
            novo_status = True
        
        cliente.alterar_dados(novo_nome, novo_cpf, novo_telefone)
        cliente.status = novo_status
        print("Alterado com sucesso")