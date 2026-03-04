from ui.menu_cliente import menu_cliente
from ui.menu_medico import menu_medico
from ui.menu_medicamento import menu_medicamento
from ui.cadastro_receita import nova_receita
from ui.menu_lista_diaria import menu_lista


def menu_principal():
     while True:
        print("\n--- MENU ---")
        print("1 - Cliente")
        print("2 - Medico")
        print("3 - Medicamento")
        print("4 - Cadastrar Receita")
        print("5 - Lista Diaria")
        print("0 - Sair")

        opcao = input("Escolha: ")

        match opcao:
            case "1":
                menu_cliente()
            case "2":
                menu_medico()
            case "3":
                menu_medicamento()
            case "4":
                nova_receita()
            case "5":
                menu_lista()
            case "0":
                break
            case _:
                print("Opção inválida.")