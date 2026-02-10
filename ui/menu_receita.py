from services.receita_service import cadastrar_receita, consultar_receita, alterar_receita


def menu_receita():
     while True:
        print("\n--- MENU RECEITA ---")
        print("1 - Cadastrar receita")

        opcao = input("Escolha: ")

        match opcao:
            case "1":
                cadastrar_receita()
            case "0":
                return
            case _:
                print("Opção inválida.")