from repositories.item_receita_repo import consultar_medicamentos_por_receita_id, adicionar_item_receita, apagar_item_receita


def consultar_medicamentos_por_receita(receita):
    itens = consultar_medicamentos_por_receita_id(receita.id)
    return itens

def inserir_item_receita(receita_id, medicamento_id, quantidade, unidade):
    adicionar_item_receita(receita_id, medicamento_id, quantidade, unidade)

def remover_item_receita(receita_id, medicamento_id):
    apagar_item_receita(receita_id, medicamento_id)




