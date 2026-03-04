from services.medicamento_service import cadastrar_medicamento, consultar_medicamento, alterar_medicamento
from utils.formatacao import padronizar_nome

def menu_medicamento():
    while True:
        print("\n--- MENU MEDICAMENTO ---")
        print("1 - Cadastrar medicamento")
        print("2 - Consultar medicamento")
        print("3 - Alterar medicamento")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        match opcao:
            case "1":
                nome = padronizar_nome(input("Informe o nome do medicamento: "))
                dosagem = input("Informe a dosagem (Ex: 20 mg): ")
                try:
                    cadastrar_medicamento(nome, dosagem)
                    print("Medicamento cadastrado com sucesso")
                except Exception as e:
                    print(str(e))
                    return
                
            case "2":
                nome = padronizar_nome(input("Informe o nome do medicamento: "))
                medicamentos = consultar_medicamento(nome)

                if not medicamentos:
                    print("Nenhum medicamento encontrado")
                    continue

                print("\nMedicamentos encontrados:")
                for med in medicamentos:
                    print(f"{med.nome} - {med.dosagem}")

            case "3":
                nome = padronizar_nome(input("Informe o nome do medicamento: "))
                medicamentos = consultar_medicamento(nome)

                if not medicamentos:
                    print("Nenhum medicamento encontrado")
                    continue

                if len(medicamentos) == 1:
                    medicamento = medicamentos[0]
                else:
                    print("\nMedicamentos encontrados:")
                    for i, med in enumerate(medicamentos, start=1):
                        print(f"{i} - {med.nome} - {med.dosagem}")

                    escolha = int(input("Escolha o medicamento: "))
                    medicamento = medicamentos[escolha - 1]

                novo_nome = padronizar_nome(input("Informe o novo nome: "))
                nova_dosagem = input("Informe a nova dosagem (Ex: 20 mg): ")

                try:
                    alterar_medicamento(novo_nome, nova_dosagem, medicamento)
                    print("Medicamento alterado com sucesso")
                except Exception as e:
                    print(str(e))
                    return
                
            case "0":
                return

            case _:
                print("Opção inválida.")