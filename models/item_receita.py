class ItemReceita:
    def __init__(self, receita, medicamento, quantidade, unidade):
        self.receita = receita
        self.medicamento = medicamento
        self.quantidade = quantidade
        self.unidade = unidade
    
    def descrição(self):
        return f"{self.medicamento.nome} {self.medicamento.dosagem} - {self.quantidade} {self.unidade}"