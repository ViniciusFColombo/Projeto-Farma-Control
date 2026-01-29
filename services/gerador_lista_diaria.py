from models.lista_diaria import ListaDiaria

class GeradorListaDiaria:
    def __init__(self, receitas):
        self.receitas = receitas

    def gerar(self, data):
        lista = ListaDiaria(
            id=None,
            data_lista=data,
            status="pendente"
        )

        for receita in self.receitas:
            if receita.pode_entrar_lista():
                lista.adicionar_receita(receita)

        return lista

class ListaReceita:
    def __init__(self, lista_id, receita_id):
        self.lista_id = lista_id
        self.receita_id = receita_id