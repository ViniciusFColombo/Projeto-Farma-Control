from repositories.medicamento_repo import buscar_medicamento_por_nome, inserir_medicamento, atualizar_medicamento


def cadastrar_medicamento(nome, dosagem):
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio.")

    inserir_medicamento(nome, dosagem)
    
def consultar_medicamento(nome):
    return buscar_medicamento_por_nome(nome)
    
def alterar_medicamento(novo_nome, nova_dosagem, medicamento):
    atualizar_medicamento(novo_nome, nova_dosagem, medicamento)

