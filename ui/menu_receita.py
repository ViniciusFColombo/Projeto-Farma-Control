from services.receita_service import cadastrar_receita, consultar_receita, alterar_receita


def menu_receita():
     while True:
        print("\n--- MENU RECEITA ---")
        print("1 - Cadastrar receita")
        print("2 - Consultar receita")
        print("3 - Alterar receita")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        match opcao:
            case "1":
                cadastrar_receita()
            case "2":
                consultar_receita()
            case "3":
                alterar_receita()
            case "0":
                return
            case _:
                print("Opção inválida.")