from repositories.medico_repo import buscar_medico_por_nome, buscar_medico_por_crm, inserir_medico, atualizar_medico
from exceptions.medico_exceptions import MedicoJaExiste, MedicoNaoEncontrado


def cadastrar_medico(nome, crm):
   if not nome.strip():
        raise ValueError("Nome não pode ser vazio.")
   
   medico_existente = buscar_medico_por_crm(crm)
   if medico_existente:
       raise MedicoJaExiste("Já existe Medico com esse CRM")
   
   inserir_medico(nome, crm)

def consultar_medico_por_nome(nome):
    medicos = buscar_medico_por_nome(nome)
    if not medicos:
        raise MedicoNaoEncontrado("Nenhum Médico encontrado")
    return medicos

def consultar_medico_por_crm(crm):
    medico = buscar_medico_por_crm(crm)
    if not medico:
        raise MedicoNaoEncontrado("Nenhum Médico encontrado")
    return medico

def alterar_medico(medico, novo_nome, novo_crm):
    if not novo_nome.strip():
        raise ValueError("Nome não pode estar vazio")
    
    medico_existente = buscar_medico_por_crm(novo_crm)

    if medico_existente and medico_existente.id != medico.id:
        raise MedicoJaExiste("Já existe outro médico com esse CRM")
    
    atualizar_medico(medico, novo_nome, novo_crm)




