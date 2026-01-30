from models.medicamento import Medicamento
from repositories.medicamento_repo import medicamentos

def cadastrar_medicamento():
    id = len (medicamentos) + 1
    nome = input("Nome do medicamento: ")
    dosagem = input("Dosagem do medicamento: ")

    medicamento = Medicamento(id, nome, dosagem)
    medicamentos.append(medicamento)
    print("Cadastro realizado com sucesso")

def consultar_medicamento():
    id = int (input("Insira o ID do medicamento: "))
    for medicamento in medicamentos:
        if medicamento.id == id:
            print(f"ID: {medicamento.id}")
            print(f"Nome: {medicamento.nome} - {medicamento.dosagem}")
            return medicamento
    print("Medicamento não encontrado")
    return None

def alterar_medicamento():
    medicamento = consultar_medicamento()

    if medicamento:
        novo_nome = input("Novo nome: ")
        nova_dosagem = input("Nova dosagem: ")

        medicamento.alterar_dados(novo_nome, nova_dosagem)
        print("Alterado com Sucesso")