class Medico:
    def __init__(self, id, nome, crm):
        self.id = id
        self.nome = nome
        self.crm = crm
    
    def alterar_dados(self, nome, crm):
        self.nome = nome
        self.crm = crm
        return "Alterado com sucesso"