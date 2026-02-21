from services.medico_service import cadastrar_medico, alterar_medico, consultar_medico_por_crm, consultar_medico_por_nome
from utils.formatacao import padronizar_nome, somente_numeros


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
                try:
                    nome = padronizar_nome(input("Nome do medico: "))
                    crm = somente_numeros(input("CRM do medico: "))
                    cadastrar_medico(nome, crm)
                    print("Medico cadastrado com sucesso!")
                except Exception as e:
                    print(f"Erro: {e}")

            case "2":
                medico = escolher_medico()
                if not medico:
                    print("Nenhum medico encontrado")
                    continue

                print(f" {medico.nome} | CRM: {medico.crm}")

            case "3":
                try:
                    medico = escolher_medico()
                    if not medico:
                        print("Nenhum medico encontrado")
                        continue

                    novo_nome = padronizar_nome(input("Novo nome: "))
                    novo_crm = somente_numeros(input("Novo CRM: "))
                    alterar_medico(medico, novo_nome, novo_crm)
                    print("Medico alterado com sucesso")
                except Exception as e:
                    print(f"Erro: {e}")

            case "0":
                return
            case _:
                print("Opção inválida.")

def escolher_medico():
    try:
        opcao = int(input("Buscar por  1 - Nome ou 2 - CRM: "))
        if opcao == 1:
            nome = padronizar_nome(input("Informe o nome do medico: "))
            medicos = consultar_medico_por_nome(nome)
   
            if len(medicos) == 1:
                return medicos[0]
            
            print("\nMedicos encontrados:")
            for i, medico in enumerate(medicos, start=1):
                print(f"{i} - {medico.nome} | CRM: {medico.crm}")
            
            escolha = int(input("Escolha o medico: "))
            return medicos[escolha - 1]
        
        elif opcao == 2:
            crm = somente_numeros(input("Informe o CRM do medico: "))
            return consultar_medico_por_crm(crm)
        
        else:
            print("Opção invalida")
            return
    except Exception as e:
        print(f"Erro:{e}")
        return None