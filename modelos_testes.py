# from datetime import datetime, timedelta

# from models.cliente import Cliente
# from models.medico import Medico
# from models.medicamento import Medicamento
# from models.receita import Receita
# from models.item_receita import ItemReceita
# from models.lista_diaria import ListaDiaria

# cliente = Cliente(
#     id=1,
#     nome="João da Silva",
#     cpf="12345678900",
#     telefone="11999999999",
#     status=True
# )

# medico = Medico(
#     id=1,
#     nome="Dr. Carlos",
#     crm="CRM12345"
# )

# losartana = Medicamento(
#     id=1,
#     nome="Losartana",
#     dosagem="50 mg"
# )

# insulina = Medicamento(
#     id=2,
#     nome="Insulina",
#     dosagem="10 ml"
# )
# item1 = ItemReceita(
#     receita=None,  # depois vinculamos
#     medicamento=losartana,
#     quantidade=60,
#     unidade="comprimidos"
# )

# item2 = ItemReceita(
#     receita=None,
#     medicamento=insulina,
#     quantidade=1,
#     unidade="frasco"
# )

# data_receita = datetime.now() - timedelta(days=150)

# receita = Receita(
#     id=1,
#     cliente=cliente,
#     medico=medico,
#     data_receita=data_receita,
#     data_ultima_retirada=None,
#     proxima_data=None,
#     status_vencida=False,
#     itens=[item1, item2]
# )

# # Testando vencimento e ultimo mes
# receita.verificar_vencimento()

# print("Receita vencida?", receita.status_vencida)
# print("Está no último mês?", receita.ultimo_mes())

# # Testando retirada
# print("\nRegistrando retirada...")
# receita.registrar_retirada()

# print("Data última retirada:", receita.data_ultima_retirada)
# print("Próxima data:", receita.proxima_data)

# # Criando lista
# lista = ListaDiaria(
#     id=1,
#     data_lista=datetime.now(),
#     status="pendente"
# )

# # Verificando se entra na lista
# if receita.pode_entrar_lista():
#     lista.adicionar_receita(receita)

# # # Exibindo a lista
# print("\nLista do dia:")
# for r in lista.listar_receitas():
#     print(f"- Cliente: {r.cliente.nome}")
#     print(f"  Médico: {r.medico.nome}")
#     for item in r.itens:
#         print(f"  {item.medicamento.nome} - {item.quantidade} {item.unidade}")
 
