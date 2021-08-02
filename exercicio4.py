import csv
with open("numeros.csv", "w") as arquivo:
	writer = csv.writer(arquivo)
	writer.writerow(("Maciel","Terra","Paiva"))
	writer.writerow(("Dara","de Lima","Monteiro"))

with open("numeros.csv","r") as arquivo:
	leitor = csv.reader(arquivo)
	for x in leitor:
		print("numero de colunas: ", len(x))
		print(x)

with open("numeros.csv","r") as arquivo:
	leitor = csv.reader(arquivo)
	dados = list(leitor)
print(dados)