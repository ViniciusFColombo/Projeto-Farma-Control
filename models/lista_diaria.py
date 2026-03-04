class ListaDiaria:
    def __init__(self, id, data_lista, status):
        self.id = id
        self.data_lista = data_lista
        self.status = status
        self.itens = []  

    def adicionar_item(self, item):
        self.itens.append(item)

    def listar_itens(self):
        return self.itens

    def fechar(self):
        self.status = "FECHADA"

    def abrir(self):
        self.status = "ABERTA"