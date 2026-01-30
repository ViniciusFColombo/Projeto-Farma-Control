medicos = []

def buscar_medico_por_id(id):
    for medico in medicos:
        if medico.id == id:
            return medico
    return None