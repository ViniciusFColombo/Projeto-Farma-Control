class Cliente:
    def __init__(self, id, nome, cpf, telefone, status):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.status = status

    def ativar(self):
        self.status = True
        return "Ativo"
    
    def desativar(self):
        self.status = False

        return "Desativado"
    def alterar_dados(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        return "Alterado com sucesso"
    
    def cliente_ativo(self):
        return self.status
    