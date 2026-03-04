from repositories.item_receita_repo import consultar_medicamentos_por_receita_id, adicionar_item_receita, apagar_item_receita


def consultar_medicamentos_por_receita(receita_id):
    return consultar_medicamentos_por_receita_id(receita_id)


def inserir_item_receita(receita_id, medicamento_id, quantidade, unidade):
    if quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero.")

    if not unidade.strip():
        raise ValueError("Unidade é obrigatória.")

    try:
        adicionar_item_receita(receita_id, medicamento_id, quantidade, unidade)
    except Exception as e:
        raise Exception("Erro ao adicionar item na receita.") from e

def remover_item_receita(receita_id, medicamento_id):
    try:
     apagar_item_receita(receita_id, medicamento_id)
    except Exception as e:
        raise Exception("Erro ao criar lista diária.") from e



