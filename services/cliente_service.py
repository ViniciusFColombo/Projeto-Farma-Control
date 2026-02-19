from repositories import cliente_repo


def cadastrar_cliente(nome, cpf, telefone):
    cliente_repo.inserir_cliente(nome, cpf, telefone)

def buscar_cliente_por_nome(nome):
    return cliente_repo.listar_cliente_por_nome(nome)

def buscar_cliente_por_cpf(cpf):
    return cliente_repo.listar_cliente_por_cpf(cpf)

def alterar_cliente(nome, cpf, telefone, status, cliente_id):
    cliente_repo.ataulizar_cliente(nome, cpf, telefone, status, cliente_id)


