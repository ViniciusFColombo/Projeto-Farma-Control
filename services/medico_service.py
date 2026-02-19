from repositories.medico_repo import buscar_medico_por_nome, buscar_medico_por_crm, inserir_medico, atualizar_medico


def cadastrar_medico(nome, crm):
   inserir_medico(nome, crm)

def consultar_medico_por_nome(nome):
    return buscar_medico_por_nome(nome)

def consultar_medico_por_crm(crm):
    return buscar_medico_por_crm(crm)

def alterar_medico(novo_nome, novo_crm, medico):
    atualizar_medico(novo_nome, novo_crm, medico)




