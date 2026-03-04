from repositories.medicamento_repo import buscar_medicamento_por_nome, inserir_medicamento, atualizar_medicamento


def cadastrar_medicamento(nome, dosagem):
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio.")

    try:
        inserir_medicamento(nome, dosagem)
    except Exception as e:
        raise Exception("Erro ao cadastrar medicamento.") from e
def consultar_medicamento(nome):
    return buscar_medicamento_por_nome(nome)
    
def alterar_medicamento(novo_nome, nova_dosagem, medicamento):
    try:
        atualizar_medicamento(novo_nome, nova_dosagem, medicamento)
    except Exception as e:
        raise Exception("Erro ao alterar medicamento.") from e
