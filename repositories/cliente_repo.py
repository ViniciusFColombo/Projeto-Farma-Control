from database.connection import get_connection
from models.cliente import Cliente

def inserir_cliente(nome, cpf, telefone):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = """
        INSERT INTO cliente (nome, cpf, telefone, status)
        VALUES (?, ?, ?, ?)
    """

    cursor.execute(comando_sql, (nome, cpf, telefone, 1))

    conn.commit()
    conn.close()

def ataulizar_cliente(nome, cpf, telefone, status, cliente_id):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = """
        UPDATE cliente
        SET nome = ?, cpf = ?, telefone = ?, status = ?
        WHERE id = ?
    """

    cursor.execute(comando_sql, (nome, cpf, telefone, int(status), cliente_id))

    conn.commit()
    conn.close()

def buscar_cliente_por_id(id):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("SELECT * FROM cliente WHERE id = ?")

    cursor.execute(comando_sql, (id,))
    row = cursor.fetchone()

    conn.close()

    if not row:
        return None

    return Cliente(
        id=row[0],
        nome=row[1],
        cpf=row[2],
        telefone=row[3],
        status=bool(row[4])
    )

def listar_cliente_por_nome(nome):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("""SELECT id, nome, cpf, telefone, status
                   FROM cliente
                   WHERE nome LIKE ?""")
    
    cursor.execute(comando_sql, (f"%{nome}%",))
    rows = cursor.fetchall()

    conn.close()
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
        return clientes

def listar_cliente_por_cpf(cpf):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = ("SELECT * FROM cliente WHERE cpf = ?")

    cursor.execute(comando_sql, (cpf,))
    row = cursor.fetchone()

    conn.close()

    if not row:
        return None

    return Cliente(
        id=row[0],
        nome=row[1],
        cpf=row[2],
        telefone=row[3],
        status=bool(row[4])
    )