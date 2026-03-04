from services import gerador_lista_diaria_service
from datetime import datetime


def menu_lista():
    while True:
        print("\n--- MENU LISTA DIARIA ---")
        print("1 - Gerar lista diaria")
        print("2 - Visualizar lista diaria")
        print("3 - Atualizar lista diaria")
        print("4 - Consultar listas geradas")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        match opcao:

            # ---------------------------------------------------------
            case "1":
                data = datetime.now().date()
                receitas = gerador_lista_diaria_service.buscar_receitas_para_lista(data)

                if not receitas:
                    print("Nenhum cliente para pegar medicamentos nesse dia")
                    continue

                try:
                    lista_id = gerador_lista_diaria_service.gerar_lista(data, "ABERTA")
                    print("Lista criada com sucesso!")

                    gerador_lista_diaria_service.adicionar_receita_na_lista(
                        lista_id,
                        receitas,
                        "PENDENTE"
                    )

                except Exception as e:
                    gerador_lista_diaria_service.excluir_lista(lista_id)
                    print("Erro ao adicionar receitas. Lista removida.")
                    print(str(e))
                    continue

                for receita_id in receitas:
                    dados = gerador_lista_diaria_service.consultar_receita_por_id(receita_id)
                    medicamentos = gerador_lista_diaria_service.buscar_medicamento_por_receita_id(receita_id)

                    print("\n------------------------------------------")
                    print(f"Nome: {dados.cliente.nome} - CPF: {dados.cliente.cpf}")
                    print(f"Medico: {dados.medico.nome} - CRM: {dados.medico.crm}")
                    print(f"Data da Receita: {dados.data_receita}")
                    print("\nMedicamentos:")

                    for item in medicamentos:
                        print(f"{item.medicamento.nome} {item.medicamento.dosagem} - {item.quantidade} {item.unidade}")

                    print("\n------------------------------------------")

            # ---------------------------------------------------------
            case "2":
                data = datetime.now().date()
                lista_diaria = gerador_lista_diaria_service.consultar_lista(data)

                if not lista_diaria:
                    print("Nenhuma lista encontrada para hoje.")
                    continue

                receitas = gerador_lista_diaria_service.consultar_receitas_da_lista(lista_diaria.id)

                if not receitas:
                    print("Nenhum cliente para pegar medicamentos nesse dia")
                    continue

                for receita in receitas:
                    medicamentos = gerador_lista_diaria_service.buscar_medicamento_por_receita_id(
                        receita["receita_id"]
                    )

                    print("\n------------------------------------------")
                    print(f"Nome: {receita['cliente_nome']} - CPF: {receita['cliente_cpf']}")
                    print(f"Médico: {receita['medico_nome']} - CRM: {receita['medico_crm']}")
                    print(f"Data da Receita: {receita['data_receita']}")
                    print("\nMedicamentos:")

                    for item in medicamentos:
                        print(f"{item.medicamento.nome} {item.medicamento.dosagem} - {item.quantidade} {item.unidade}")

                    print("\n------------------------------------------")

            # ---------------------------------------------------------
            case "3":

                data = datetime.now().date()
                lista_diaria = gerador_lista_diaria_service.consultar_lista(data)

                if not lista_diaria:
                    print("Nenhuma lista encontrada para hoje.")
                    continue

                receitas = gerador_lista_diaria_service.consultar_receitas_da_lista(lista_diaria.id)

                if not receitas:
                    print("Nenhum cliente para pegar medicamentos nesse dia")
                    continue

                marcacoes = []

                for receita in receitas:
                    print("\n------------------------------------------")
                    print(f"Nome: {receita['cliente_nome']} - CPF: {receita['cliente_cpf']}")
                    escolha = input("Marcar como: 1 - Retirado / 2 - Adiado: ")

                    if escolha == "1":
                        marcacoes.append({
                            "receita_id": receita["receita_id"],
                            "status": "RETIRADO"
                        })
                    elif escolha == "2":
                        marcacoes.append({
                            "receita_id": receita["receita_id"],
                            "status": "ADIADO"
                        })
                    else:
                        print("Opção inválida.")

                if not marcacoes:
                    print("Nenhuma marcação realizada.")
                    continue

                confirmacao = input("Confirmar salvamento? (s/n): ")

                if confirmacao.lower() == "s":
                    try:
                        gerador_lista_diaria_service.processar_fechamento_lista(
                            lista_diaria.id,
                            marcacoes
                        )
                        print("Lista finalizada com sucesso!")
                    except Exception as e:
                        print(str(e))
                else:
                    print("Operação cancelada.")

            # ---------------------------------------------------------
            case "4":
                data_str = input("Data da lista (dd/mm/aaaa): ")

                try:
                    data = datetime.strptime(data_str, "%d/%m/%Y").date()
                except ValueError:
                    print("Data inválida.")
                    continue

                lista_diaria = gerador_lista_diaria_service.consultar_lista(data)

                if not lista_diaria:
                    print("Nenhuma lista encontrada nessa data.")
                    continue

                print(f"\nID: {lista_diaria.id}")
                print(f"Data: {lista_diaria.data_lista}")
                print(f"Status: {lista_diaria.status}")

                escolha = input("Deseja ver a lista detalhada (s/n): ")

                if escolha.lower() == "s":

                    receitas = gerador_lista_diaria_service.consultar_receitas_da_lista(lista_diaria.id)

                    if not receitas:
                        print("Nenhum cliente na lista.")
                        continue

                    for receita in receitas:
                        medicamentos = gerador_lista_diaria_service.buscar_medicamento_por_receita_id(
                            receita["receita_id"]
                        )

                        print("\n------------------------------------------")
                        print(f"Nome: {receita['cliente_nome']} - CPF: {receita['cliente_cpf']}")
                        print(f"Médico: {receita['medico_nome']} - CRM: {receita['medico_crm']}")
                        print(f"Data da Receita: {receita['data_receita']}")
                        print("\nMedicamentos:")

                        for item in medicamentos:
                            print(f"{item.medicamento.nome} {item.medicamento.dosagem} - {item.quantidade} {item.unidade}")

                        print("\n------------------------------------------")

            # ---------------------------------------------------------
            case "0":
                return

            # ---------------------------------------------------------
            case _:
                print("Opção inválida.")