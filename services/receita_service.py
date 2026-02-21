from repositories.receita_repo import buscar_receita_cliente_id, inserir_receita, atualizar_data_receita, atualizar_medico_receita, atualizar_data_retirada
from datetime import datetime

def cadastrar_receita(cliente, medico, data_receita, itens):
    if not data_receita:
        raise ValueError("Data da receita é obrigatória.")

    if data_receita > datetime.now():
        raise ValueError("Data da receita não pode ser no futuro.")

    if not itens:
        raise ValueError("Receita deve conter pelo menos um medicamento.")

    inserir_receita(cliente, medico, data_receita, itens)


def consultar_receita(cliente_id):
    return buscar_receita_cliente_id(cliente_id)


def alterar_medico_receita(receita, novo_medico):
    atualizar_medico_receita(receita, novo_medico)


def alterar_data_receita(receita, nova_data):
    if not nova_data:
        raise ValueError("Data da receita é obrigatória.")

    if nova_data > datetime.now():
        raise ValueError("Data da receita não pode ser no futuro.")

    atualizar_data_receita(receita, nova_data)


def alterar_retirada(receita, nova_data):
    if not nova_data:
        raise ValueError("Data de retirada é obrigatória.")

    if nova_data < receita.data_receita:
        raise ValueError("Data de retirada não pode ser antes da data da receita.")

    receita.alterar_retirada(nova_data)

    atualizar_data_retirada(
        receita.id,
        receita.data_ultima_retirada,
        receita.proxima_data
    )

    return receita

    
