from services.medicamento_service import cadastrar_medicamento, consultar_medicamento, alterar_medicamento

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
                cadastrar_medicamento()
            case "2":
                consultar_medicamento()
            case "3":
                alterar_medicamento()
            case "0":
                return
            case _:
                print("Opção inválida.")