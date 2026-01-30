from services.medico_service import cadastrar_medico, consultar_medico, alterar_medico


def menu_medico():
     while True:
        print("\n--- MENU MÉDICO ---")
        print("1 - Cadastrar médico")
        print("2 - Consultar médico")
        print("3 - Alterar médico")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        match opcao:
            case "1":
                cadastrar_medico()
            case "2":
                consultar_medico()
            case "3":
                alterar_medico()
            case "0":
                return
            case _:
                print("Opção inválida.")