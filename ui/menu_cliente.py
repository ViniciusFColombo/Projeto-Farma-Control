from services.cliente_service import cadastrar_cliente, consultar_cliente, alterar_cliente

def menu_cliente():
     while True:
        print("\n--- MENU CLIENTE ---")
        print("1 - Cadastrar cliente")
        print("2 - Consultar cliente")
        print("3 - Alterar cliente")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        match opcao:
            case "1":
                cadastrar_cliente()
            case "2":
                consultar_cliente()
            case "3":
                alterar_cliente()
            case "0":
                return
            case _:
                print("Opção inválida.")