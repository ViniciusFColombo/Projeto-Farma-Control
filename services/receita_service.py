from repositories.receita_repo import buscar_receita_cliente_id, inserir_receita, atualizar_data_receita, atualizar_medico_receita, atualizar_data_retirada
from database.connection import get_connection


def cadastrar_receita(cliente, medico, data_receita, itens):
     inserir_receita(cliente, medico, data_receita, itens)

def consultar_receita(cliente_id):
    return buscar_receita_cliente_id(cliente_id)

def alterar_medico_receita(receita, novo_medico):
    atualizar_medico_receita(receita, novo_medico)
    
def alterar_data_receita(receita, nova_data):
    atualizar_data_receita(receita, nova_data)
  
def alterar_retirada(receita, nova_data):
    receita.alterar_retirada(nova_data)

    atualizar_data_retirada(
        receita.id,
        receita.data_ultima_retirada,
        receita.proxima_data
    )

    return receita

    
