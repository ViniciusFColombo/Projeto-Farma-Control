clientes = []

def buscar_cliente_por_id(id):
    for cliente in clientes:
        if cliente.id == id:
            return cliente
    return None