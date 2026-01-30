receitas = []

def buscar_receita_por_id(id):
    for receita in receitas:
        if receita.id == id:
            return receita
    return None