class ListaDiaria:
    def __init__(self, id, data_lista, status):
        self.id = id
        self.data_lista = data_lista
        self.status = status
        self.receitas = []

    def adicionar_receita(self, receita):
        self.receitas.append(receita)

    def confirmar(self):
        self.status = "confirmada"

    def pendente(self):
        self.status = "pendente"

    def listar_receitas(self):
        return self.receitas