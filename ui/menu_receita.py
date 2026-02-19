from services.item_receita_service import consultar_medicamentos_por_receita, inserir_item_receita, remover_item_receita
from services.receita_service import alterar_retirada, alterar_data_receita, alterar_medico_receita, consultar_receita
from services.medico_service import consultar_medico_por_nome, consultar_medico_por_crm
from services.medicamento_service import consultar_medicamento
from utils.formatacao import padronizar_nome, somente_numeros
from datetime import datetime

def menu_receita(cliente_id):
    

    while True:
        receitas = consultar_receita(cliente_id)

        if not receitas:
            print("Nenhuma receita encontrada.")
        print("\n--- RECEITAS ---")

        for i, receita in enumerate(receitas):
            print("\n----------------------")
            print(f"{i + 1}")
            print(f"Médico: {receita.medico.nome} | CRM: {receita.medico.crm}")
            print(f"Data: {receita.data_receita.strftime('%d/%m/%Y')}")
            print(f"Data da ultima retirada: {receita.data_ultima_retirada.strftime('%d/%m/%Y') if receita.data_ultima_retirada else '---'}")
            print(f"Proxima data de retirada: {receita.proxima_data.strftime('%d/%m/%Y') if receita.proxima_data else '---'}")
            print(f"Status: {'Vencida' if receita.status_vencida else 'Ativa'}")

        print("\n1 - Visualizar receita")
        print("2 - Alterar receita")
        print("3 - Registrar ou Alterar retirada")
        print("0 - Voltar")

        opcao_receita = input("Escolha: ")

        match opcao_receita:
            case "1":
                num = int(input("Escolha a receita: "))
                receita_escolhida = receitas[num - 1]

                itens = consultar_medicamentos_por_receita(receita_escolhida)

                for i, item in enumerate(itens):
                    print("\n----------------------")
                    print(f"{i + 1}")
                    print(f"{item.medicamento.nome} {item.medicamento.dosagem} {item.quantidade} {item.unidade}")

            case "2":
                num = int(input("Escolha a receita: "))
                receita_escolhida = receitas[num - 1]

                menu_alterar(receita_escolhida)

            case "3":
                num = int(input("Escolha a receita: "))
                receita_escolhida = receitas[num - 1]

                data_str = input("Informa a nova data de retirada (dd/mm/aaaa): ")
                nova_data = datetime.strptime(data_str, "%d/%m/%Y")

                alterar_retirada(receita_escolhida, nova_data)

            case "0":
                return

            case _:
                print("Opção inválida.")

def menu_alterar(receita_escolhida):
    print("\n1 - Alterar data da receita")
    print("2 - Alterar medico da receita")
    print("3 - Adicionar medicamento")
    print("4 - Remover medicamento")
    print("0 - Voltar")

    opcao = input("Escolha: ")

    match opcao:
        case "1":
            data_str = input("Informa a nova data (dd/mm/aaaa): ")
            nova_data = datetime.strptime(data_str, "%d/%m/%Y")
            alterar_data_receita(receita_escolhida, nova_data)
            print("Receita alterada com sucesso")
        
        case "2":
            opcao = int(input("Deseja procurar por 1 - Nome ou 2 - CRM: "))
            if opcao == 1:
                nome = padronizar_nome(input("Informe o nome do medico: "))
                medicos = consultar_medico_por_nome(nome)

                if not medicos:
                    print("Nenhum medico encontrado")
                    return

                for i, medico in enumerate(medicos):
                    print(f"{i + 1} - Nome: {medico.nome} | CRM: {medico.crm}")

                escolha = int(input("Escolha o medico: ")) - 1
                novo_medico = medicos[escolha]
                alterar_medico_receita(receita_escolhida.id, novo_medico)
                print("Alterado com sucesso")
            elif opcao == 2:
                novo_medico = somente_numeros(input("Informe o CRM do medico: "))
                consultar_medico_por_crm(novo_medico)
                alterar_medico_receita(receita_escolhida, novo_medico)
                print("Alterado com sucesso")
            else:
                print("Opção invalida")
                return
        
        case "3":
            medicamento = padronizar_nome(input("Informe o nome do medicamento: "))
            medicamentos = consultar_medicamento(medicamento)
            if not medicamentos:
                print("Nenhum medicamento encontrado")
                return 
        
            for i, med in enumerate(medicamentos):
                print(f"{i + 1} - Nome: {med.nome} {med.dosagem}")
            escolha = int(input("Escolha o medicamento: ")) - 1
            quantidade = int(input("Quantidade: "))
            unidade = input("Unidade: ")
            inserir_item_receita(receita_escolhida.id, medicamentos[escolha].id, quantidade, unidade)
            print("Medicamento adicionado com sucesso")

        case "4":
            itens = consultar_medicamentos_por_receita(receita_escolhida)

            if not itens:
                print("Nenhum item para remover")
                return

            for i, item in enumerate(itens, start=1):
                print(f"{i} - {item.medicamento.nome}")

            escolha = int(input("Escolha o item para remover: ")) - 1

            item = itens[escolha]

            remover_item_receita(receita_escolhida, item)
            print("Medicamento removido com sucesso")

        case "0":
            return

        case _:
            print("Opção inválida")


            

