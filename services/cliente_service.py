from repositories import cliente_repo
from exceptions.cliente_exceptions import ClienteJaExiste, ClienteNaoEncontrado, CPFInvalido


def cadastrar_cliente(nome, cpf, telefone):

    if not nome.strip():
        raise ValueError("Nome não pode ser vazio.")

    if len(cpf) != 11:
        raise CPFInvalido("CPF deve conter 11 dígitos.")

    cliente_existente = cliente_repo.listar_cliente_por_cpf(cpf)
    if cliente_existente:
        raise ClienteJaExiste("Já existe cliente com esse CPF.")

    cliente_repo.inserir_cliente(nome, cpf, telefone)


def buscar_cliente_por_nome(nome):
    clientes = cliente_repo.listar_cliente_por_nome(nome)

    if not clientes:
        raise ClienteNaoEncontrado("Nenhum cliente encontrado com esse nome.")

    return clientes


def buscar_cliente_por_cpf(cpf):
    cliente = cliente_repo.listar_cliente_por_cpf(cpf)

    if not cliente:
        raise ClienteNaoEncontrado("Cliente não encontrado.")

    return cliente


def alterar_cliente(cliente_id, nome, cpf, telefone, status):

    if not nome.strip():
            raise ValueError("Nome não pode ser vazio.")
    
    if len(cpf) != 11:
        raise CPFInvalido("CPF deve conter 11 dígitos.")
    
    cliente_existente = cliente_repo.listar_cliente_por_cpf(cpf)

    if cliente_existente and cliente_existente.id != cliente_id:
        raise ClienteJaExiste("Já existe outro cliente com esse CPF.")

    cliente_repo.ataulizar_cliente(cliente_id, nome, cpf, telefone, status)