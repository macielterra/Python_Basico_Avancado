import json
import csv

with open("dados.json", "r") as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)
print(dados)

with open("file.csv", "r") as arquivo:
    texto = csv.reader(arquivo)
    dados = (texto)
print(dados)