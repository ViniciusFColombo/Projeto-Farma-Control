
from models.cliente import Cliente
from services.item_receita_service import consultar_medicamentos_por_receita
from utils.filtros_pesquisas import listar_cliente_por_nome, listar_cliente_por_cpf
from database.connection import get_connection
from utils.formatacao import padronizar_nome, formatar_cpf, formatar_telefone, somente_numeros
from services.receita_service import consultar_receita, alterar_retirada, alterar_receita

def escolher_listagem_cliente():
    opcao = int(input("Deseja procurar por 1 - Nome ou 2 - CPF: "))
    if opcao == 1 :
        cliente = listar_cliente_por_nome()
    else :
        cliente = listar_cliente_por_cpf()
    return cliente

def cadastrar_cliente():
    nome = padronizar_nome(input("Nome do cliente: "))
    cpf = somente_numeros(input("CPF do cliente: "))
    telefone = somente_numeros(input("Telefone do cliente: "))
    status = True
    conn = get_connection()
    cursor = conn.cursor()
    
    comando_sql = ("""INSERT INTO cliente (nome, cpf, telefone, status)
                VALUES (?, ?, ?, ?)""")
    
    cursor.execute(comando_sql, (nome, cpf, telefone, int(status)))

    conn.commit()
    conn.close()
    print("Cliente cadastrado com sucesso!")

def consultar_cliente():
    cliente = escolher_listagem_cliente()
    if not cliente:
        return

    receitas = consultar_receita(cliente.id)

    for i, receita in enumerate(receitas):
        print("\n----------------------")
        print(f"{i + 1}")
        print(f"Médico: {receita.medico.nome} | CRM: {receita.medico.crm}")
        print(f"Data da Receita: {receita.data_receita.strftime('%d/%m/%Y')}")
        print(f"Status: {'Vencida' if receita.status_vencida else 'Ativa'}")

    print("1 - Vizualizar receita")
    print("2 - Alterar receita")
    print("3 - Registrar ou Alterar retirada")
    print("0 - Voltar")


    opcao = int(input("Escolha: "))
    match opcao:
        case 1:
            num = int(input("Escolha a receita (1, 2, 3): "))
            indice = num - 1
            receita_escolhida = receitas[indice]

            itens =consultar_medicamentos_por_receita(receita_escolhida)
            for i, item in enumerate(itens):
                print("\n----------------------")
                print(f"{i + 1}")
                print(f"{item.medicamento.nome} {item.medicamento.dosagem} {item.quantidade} {item.unidade}")


        case 2:
            num = int(input("Escolha a receita (1, 2, 3): "))
            receita_escolhida = receitas[num - 1]

            alterar_receita(receita_escolhida)

        case 3:
            num = int(input("Escolha a receita (1, 2, 3): "))
            receita_escolhida = receitas[num - 1]

            alterar_retirada(receita_escolhida)

        case 0:
            return
        case _:
            print("Opção inválida.")

def alterar_cliente():
    cliente = escolher_listagem_cliente()

    if cliente:
        novo_nome = padronizar_nome(input("Novo nome: "))
        novo_cpf = somente_numeros(input("Novo CPF:" ))
        novo_telefone = somente_numeros(input("Novo telefone: "))
        opcao = int(input("Novo status (0 - ""Desativar""/ 1 - ""Ativar""): "))
        novo_status = True
        if opcao == 0:
            novo_status = True if opcao == 1 else False
        
        conn = get_connection()
        cursor = conn.cursor()

        comando_sql = ("""UPDATE cliente SET nome = ?, cpf = ?, telefone = ?, status = ? 
                       WHERE id = ?""")
        
        cursor.execute(comando_sql, (novo_nome, novo_cpf, novo_telefone, int(novo_status), cliente.id))
        
        conn.commit()
        conn.close()
        print("Alterado com sucesso")