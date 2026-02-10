from repositories.cliente_repo import buscar_cliente_por_nome, buscar_cliente_por_cpf
from repositories.medico_repo import buscar_medico_por_nome, buscar_medico_por_crm
from repositories.medicamento_repo import buscar_medicamento_por_nome
from utils.formatacao import somente_numeros, padronizar_nome
from models.cliente import Cliente
from models.medico import Medico
from models.medicamento import Medicamento

# Receitas para vincular com cliente
def listar_cliente_por_cpf():
    cpf = somente_numeros(input("Digite o cpf do cliente: "))
    row = buscar_cliente_por_cpf(cpf)

    if not row:
        print("Nenhum cliente encontrado")
        return None
    
    cliente = Cliente(
        id=row[0],
        nome=row[1],
        cpf=row[2],
        telefone=row[3],
        status=bool(row[4])
    )

    print(f"Nome: {cliente.nome} | CPF: {cliente.cpf} | Telefone: {cliente.telefone}")
    return cliente

def listar_cliente_por_nome():
    nome = padronizar_nome(input("Digite o nome do cliente: "))
    rows = buscar_cliente_por_nome(nome)

    if not rows:
        print("Nenhum cliente encontrado")
        return None

    clientes = []
    for row in rows:
        cliente = Cliente(
            id=row[0],
            nome=row[1],
            cpf=row[2],
            telefone=row[3],
            status=bool(row[4])
        )
        clientes.append(cliente)

    for i, cliente in enumerate(clientes):
        print(f"{i + 1} - {cliente.nome} | CPF: {cliente.cpf}")

    escolha = int(input("Escolha o cliente: ")) - 1
    return clientes[escolha]


# Receita para vincular com medico
def listar_medico_por_crm():
    crm = somente_numeros(input("Insira o CRM do medico: "))
    row = buscar_medico_por_crm(crm)

    if not row:
        print("Medico não encontrado")
        return None
    
    medico = Medico(
        id=row[0],
        nome=row[1],
        crm=row[2]
    )

    print(f"Nome: {medico.nome} | CRM: {medico.crm}")
    return medico

def listar_medico_por_nome():
    nome = padronizar_nome(input("Insira o nome do medico: "))
    rows = buscar_medico_por_nome(nome)

    if not rows:
        print("Nenhum medico encontrado")
        return None
    
    medicos =[]
    for row in rows:
        medico = Medico(
            id=row[0],
            nome=row[1],
            crm=row[2]
        )
        medicos.append(medico)
    
    for i, medico in enumerate(medicos):
        print(f"{i + 1} - Nome: {medico.nome} | CRM: {medico.crm}")
    
    escolha = int(input("Escolha o medico: ")) - 1
    return medicos[escolha]

# Medicamentos para vincular com receita

def listar_medicamento_por_nome():
    nome = padronizar_nome(input("Insira o nome do medicamento"))
    rows = buscar_medicamento_por_nome(nome)

    if not rows:
        print("Nenhum medicamento encontrado")
        return None
    
    medicamentos = []
    for row in rows:
        medicamento = Medicamento(
            id=row[0],
            nome=row[1],
            dosagem=row[2]
        )
        medicamentos.append(medicamento)

    for i, medicamento in enumerate(medicamentos):
        print(f"{i + 1} - Nome: {medicamento.nome} {medicamento.dosagem}")
        
    escolha = int(input("Escolha o medicamento: ")) - 1
    return medicamentos[escolha]