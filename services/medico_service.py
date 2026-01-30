from models.medico import Medico
from repositories.medico_repo import medicos

def cadastrar_medico():
    id = len(medicos) + 1
    nome = input("Nome do médico: ")
    crm = input("CRM: ")

    medico = Medico(id, nome, crm)
    medicos.append(medico)

    print("Médico cadastrado com sucesso!")

def consultar_medico():
    id = int(input("Digite o ID do médico: "))

    for medico in medicos:
        if medico.id == id:
            print(f"ID: {medico.id}")
            print(f"Nome: {medico.nome}")
            print(f"CRM: {medico.crm}")
            return medico

    print("Médico não encontrado.")
    return None

def alterar_medico():
    medico = consultar_medico()

    if medico:
        novo_nome = input("Novo nome: ")
        novo_crm = input("Novo CRM: ")

        medico.alterar_dados(novo_nome, novo_crm)
        print("Dados alterados com sucesso!")