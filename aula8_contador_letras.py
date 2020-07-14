def contadorLetras(lista):
    contador = []
    for i in lista:
        qtd = len(i)
        contador.append(qtd)
    return contador

    
if __name__ == "__main__":
    vet_nomes = ['cachorro','gato']
    print(contadorLetras(vet_nomes))