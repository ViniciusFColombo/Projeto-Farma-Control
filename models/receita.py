from models.cliente import Cliente
from datetime import datetime
from datetime import timedelta

class Receita:
    def __init__(self, id, cliente, medico, data_receita, data_ultima_retirada, proxima_data, status_vencida, itens):
        self.id = id
        self.cliente = cliente
        self.medico = medico
        self.data_receita = data_receita
        self.data_ultima_retirada = data_ultima_retirada
        self.proxima_data = proxima_data
        self.status_vencida = status_vencida
        self.itens = itens

    def verificar_vencimento(self):
        if ((self.data_receita + timedelta(days = 180)) < datetime.now()):
            self.status_vencida = True
        else:
            self.status_vencida = False

    def ultimo_mes(self):
        if (datetime.now() >= self.data_receita + timedelta(days = 150) and datetime.now() < self.data_receita + timedelta(days = 180)):
           return True
        else:
           return False
        
    def registrar_retirada(self):
        self.data_ultima_retirada = datetime.now()
        self.calcular_proxima_data()
        
    def alterar_retirada(self, nova_data):
        self.data_ultima_retirada = nova_data
        self.calcular_proxima_data()

    def calcular_proxima_data(self):
        self.proxima_data = self.data_ultima_retirada + timedelta(days = 30)

    def pode_entrar_lista(self):
       if (self.cliente.status and not self.status_vencida):
           return True
       else:
           return False