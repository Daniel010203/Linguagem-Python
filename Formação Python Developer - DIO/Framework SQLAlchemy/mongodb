"""
    DESAFIO DIO PARA INTEGRAÇÃO DE PYTHON COM BANCO DE DADOS
    Integraçao com MongoDB utilizando PyMongo
"""

import pymongo
import pprint

print("Iniciando a conexão com o MongoDB")

# Cria a conexão com o MongoDB
connection = pymongo.MongoClient("link-para-o-mongo-db")

# Cria o banco de dados e a collection
db = connection.bank
collection = db.clients

# Define as informações que irão compor o documento
new_clients = [{
            "agency": 1050,
            "name": "Alfred Pennieold",
            "cpf": "123.456.789.11",
            "address": "Rua 2, número 1000",
            "account": ["cc", "110501"],
            "balance": 5000
            },
            {
            "agency": 1050,
            "name": "Gordon Felicity",
            "cpf": "123.456.789.22",
            "address": "Rua 3, número 800",
            "account": ["cp", "210501"],
            "balance": 15000
            },
            {
            "agency": 2000,
            "name": "Lawrence Adamns",
            "cpf": "123.456.789.78",
            "address": "Rua 4, número 500",
            "account": ["cp", "220001"],
            "balance": 17000
            },
            {
            "agency": 2000,
            "name": "Borneis Lancaster",
            "cpf": "123.456.789.44",
            "address": "Rua 4, número 700",
            "account": ["cc", "120001"],
            "balance": 1500
            }]


print("Salvando as informações no MongoDB")
clients = db.clients
result = clients.insert_many(new_clients)
print(result.inserted_ids)


print("\n Recuperando as informações da cliente Sandy:")
pprint.pprint(db.clients.find_one({"name": "Sandy Júnior"}))


print("\n Listagem dos clientes presentes na coleção clients:")
for client in clients.find():
    pprint.pprint(client)


print("\n Recuperando informação dos clientes de maneira ordenada pelo nome:")
for client in clients.find({}).sort("name"):
    pprint.pprint(client)


print("\n Clientes da agência 2000:")
for client in clients.find({"agency": 2000}):
    pprint.pprint(client)


print("\n Clientes com conta poupança:")
for client in clients.find({"account": "cp"}):
    pprint.pprint(client)


print("\n Clientes com conta corrente:")
for client in clients.find({"account": "cc"}):
    pprint.pprint(client)
