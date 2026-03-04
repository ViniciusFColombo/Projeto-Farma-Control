from repositories import lista_diaria_repo
from repositories import lista_receita_repo
from repositories import receita_repo
from repositories import item_receita_repo


def buscar_receitas_para_lista(data):
    return receita_repo.buscar_ids_por_proxima_data_prevista(data)


def gerar_lista(data, status):
    try:
        return lista_diaria_repo.criar_lista(data, status)
    except Exception as e:
        raise Exception("Erro ao criar lista diária.") from e


def alterar_status_lista(lista_id, status):
    try:
        lista_diaria_repo.atualizar_status_lista(lista_id, status)
    except Exception as e:
        raise Exception("Erro ao atualizar status da lista.") from e


def consultar_lista(data):
    return lista_diaria_repo.buscar_lista(data)


def adicionar_receita_na_lista(lista_id, receitas, status):
    try:
        lista_receita_repo.inserir_receita_na_lista(lista_id, receitas, status)
    except Exception as e:
        raise Exception("Erro ao adicionar receitas na lista.") from e


def processar_fechamento_lista(lista_id, marcacoes):
    try:
        for item in marcacoes:
            receita_id = item["receita_id"]
            status = item["status"]

            lista_receita_repo.atualizar_status(lista_id, receita_id, status)

            if status == "ADIADO":
                receita_repo.atualizar_proxima_data_para_dia_seguinte(receita_id)

        lista_diaria_repo.atualizar_status_lista(lista_id, "CONCLUIDO")

    except Exception as e:
        raise Exception("Erro ao finalizar lista diária.") from e

def excluir_lista(lista_id):
    lista_diaria_repo.excluir_lista(lista_id)

def consultar_clientes_nao_marcados(lista_id):
    return lista_receita_repo.buscar_clientes_nao_marcados(lista_id)


def consultar_receita_por_id(receita_id):
    return receita_repo.buscar_receita_por_id(receita_id)


def buscar_medicamento_por_receita_id(receita_id):
    return item_receita_repo.consultar_medicamentos_por_receita_id(receita_id)

def consultar_receitas_da_lista(lista_id):
    rows = lista_receita_repo.buscar_receitas_completas_da_lista(lista_id)

    receitas = []

    for row in rows:
        receitas.append({
            "receita_id": row[0],
            "data_receita": row[1],
            "cliente_nome": row[2],
            "cliente_cpf": row[3],
            "medico_nome": row[4],
            "medico_crm": row[5]
        })

    return receitas