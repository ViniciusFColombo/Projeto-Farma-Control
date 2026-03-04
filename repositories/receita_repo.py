from database.connection import get_connection
from datetime import datetime, timedelta
from models.cliente import Cliente
from models.medico import Medico
from models.receita import Receita


def buscar_receita_cliente_id(cliente_id):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = """
        SELECT
            r.id,
            r.data_receita,
            r.data_ultima_retirada,
            r.proxima_data_prevista,
            r.status,
            
            c.id AS cliente_id,
            c.nome AS cliente_nome,
            c.cpf AS cliente_cpf,
            c.telefone,
            c.status AS cliente_status,

            m.id AS medico_id,
            m.nome AS medico_nome,
            m.crm

        FROM receita r
        JOIN cliente c ON c.id = r.cliente_id
        JOIN medico m ON m.id = r.medico_id
        WHERE r.cliente_id = ?
        ORDER BY r.data_receita DESC
        LIMIT 3
    """

    cursor.execute(comando_sql, (cliente_id,))
    rows = cursor.fetchall()
    conn.close()

    receitas = []

    for row in rows:
        cliente = Cliente(
            id=row["cliente_id"],
            nome=row["cliente_nome"],
            cpf=row["cliente_cpf"],
            telefone=row["telefone"],
            status=bool(row["cliente_status"])
        )

        medico = Medico(
            id=row["medico_id"],
            nome=row["medico_nome"],
            crm=row["crm"]
        )

        receita = Receita(
            id=row["id"],
            cliente=cliente,
            medico=medico,
            data_receita=datetime.strptime(row["data_receita"], "%Y-%m-%d").date(),
            data_ultima_retirada=(
                datetime.strptime(row["data_ultima_retirada"], "%Y-%m-%d").date()
                if row["data_ultima_retirada"] else None
            ),
            proxima_data=(
                datetime.strptime(row["proxima_data_prevista"], "%Y-%m-%d").date()
                if row["proxima_data_prevista"] else None
            ),
            status_vencida=True if int(row["status"]) == 1 else False,
            itens=[]
        )

        receitas.append(receita)

    return receitas


def inserir_receita(cliente, medico, data_receita, itens):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = """
            INSERT INTO receita (cliente_id, medico_id, data_receita,
            data_ultima_retirada, proxima_data_prevista, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            comando_sql,
            (cliente.id, medico.id, data_receita.strftime("%Y-%m-%d"), None, None, 0)
        )

        receita_id = cursor.lastrowid

        comando_item_sql = """
            INSERT INTO receita_medicamento
            (receita_id, medicamento_id, quantidade, unidade)
            VALUES (?, ?, ?, ?)
        """

        for item in itens:
            cursor.execute(
                comando_item_sql,
                (receita_id, item.medicamento.id, item.quantidade, item.unidade)
            )

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    return receita_id


def atualizar_data_receita(receita, nova_data):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = "UPDATE receita SET data_receita = ? WHERE id = ?"
        cursor.execute(comando_sql, (nova_data.strftime("%Y-%m-%d"), receita.id))

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    receita.data_receita = nova_data
    return receita


def atualizar_medico_receita(receita, novo_medico):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = "UPDATE receita SET medico_id = ? WHERE id = ?"
        cursor.execute(comando_sql, (novo_medico.id, receita.id))

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    receita.medico = novo_medico
    return receita


def atualizar_data_retirada(receita_id, data_ultima, proxima_data):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        comando_sql = """
            UPDATE receita
            SET data_ultima_retirada = ?, 
                proxima_data_prevista = ?
            WHERE id = ?
        """

        cursor.execute(
            comando_sql,
            (data_ultima.strftime("%Y-%m-%d"), proxima_data.strftime("%Y-%m-%d"), receita_id)
        )

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def buscar_ids_por_proxima_data_prevista(data):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = "SELECT id FROM receita WHERE proxima_data_prevista = ?"

    cursor.execute(comando_sql, (data.strftime("%Y-%m-%d"),))
    rows = cursor.fetchall()
    conn.close()

    return [row["id"] for row in rows]


def buscar_receita_por_id(receita_id):
    conn = get_connection()
    cursor = conn.cursor()

    comando_sql = """
        SELECT
            r.id,
            r.data_receita,
            r.data_ultima_retirada,
            r.proxima_data_prevista,
            r.status,
            
            c.id AS cliente_id,
            c.nome AS cliente_nome,
            c.cpf AS cliente_cpf,
            c.telefone,
            c.status AS cliente_status,

            m.id AS medico_id,
            m.nome AS medico_nome,
            m.crm

        FROM receita r
        JOIN cliente c ON c.id = r.cliente_id
        JOIN medico m ON m.id = r.medico_id
        WHERE r.id = ?
    """

    cursor.execute(comando_sql, (receita_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    cliente = Cliente(
        id=row["cliente_id"],
        nome=row["cliente_nome"],
        cpf=row["cliente_cpf"],
        telefone=row["telefone"],
        status=bool(row["cliente_status"])
    )

    medico = Medico(
        id=row["medico_id"],
        nome=row["medico_nome"],
        crm=row["crm"]
    )

    receita = Receita(
        id=row["id"],
        cliente=cliente,
        medico=medico,
        data_receita=datetime.strptime(row["data_receita"], "%Y-%m-%d").date(),
        data_ultima_retirada=(
            datetime.strptime(row["data_ultima_retirada"], "%Y-%m-%d").date()
            if row["data_ultima_retirada"] else None
        ),
        proxima_data=(
            datetime.strptime(row["proxima_data_prevista"], "%Y-%m-%d").date()
            if row["proxima_data_prevista"] else None
        ),
        status_vencida=True if int(row["status"]) == 1 else False,
        itens=[]
    )

    return receita


def atualizar_proxima_data_para_dia_seguinte(receita_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT proxima_data_prevista FROM receita WHERE id = ?",
            (receita_id,)
        )
        row = cursor.fetchone()

        if not row or not row[0]:
            raise Exception("Receita não encontrada ou sem data prevista.")

        data_atual = datetime.strptime(row[0], "%Y-%m-%d").date()
        nova_data = data_atual + timedelta(days=1)

        cursor.execute(
            "UPDATE receita SET proxima_data_prevista = ? WHERE id = ?",
            (nova_data.strftime("%Y-%m-%d"), receita_id)
        )

        conn.commit()

    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()