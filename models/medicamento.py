class Medicamento:
    def __init__(self, id, nome, dosagem):
        self.id = id
        self.nome = nome
        self.dosagem = dosagem

    def descricao_completa(self):
        return f"{self.nome} - {self.dosagem}"
    
    def alterar_dados(self, nome, dosagem):
        self.nome = nome
        self.dosagem = dosagem
        return "Alterado com sucesso"