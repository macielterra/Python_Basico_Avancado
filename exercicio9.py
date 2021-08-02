import csv
with open("file.csv", "r") as arquivo:
    texto = csv.reader(arquivo)
    dados = (texto)
print(dados)