import csv
with open("file.csv","w") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(("primeiro","segundo","terceiro"))
    writer.writerow((10,20,30))
with open("file.csv","r") as arquivo:
    leitor = csv.reader(arquivo)
    dados=list(leitor)
print(dados)

import csv
with open("file.csv","r") as arquivo:
    leitor = csv.reader(arquivo)
    dados=list(leitor)
for i in dados[1:]:
    print(i)