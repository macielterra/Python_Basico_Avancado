contador_letras = lambda lista: [len(x) for x in lista]
# na funçao lambda recebe uma lista que tera um contador (for) para contar o tamanho de cada palavra da lista
# essa funçao lambda retornara o tamanho de cada palavra da lista em forma de list

lista_animas = ['cachorro','gato','elefante']
print(contador_letras(lista_animas))

soma = lambda a,b: a+b
subtracao = lambda a,b:a-b

print(soma(5,10))
print(subtracao(10,5))

#fazendo uma calculadora com dicionario de lambdas
calculadora = {
    'soma': lambda a,b: a+b,
    'subtracao': lambda a,b: a-b,
    'multiplicacao': lambda a,b: a*b,
    'divisao': lambda a,b: a/b
}

print(type(calculadora))

soma = calculadora['soma']#acessando a funçao lambda do id soma no dic calculadora
multiplicacao = calculadora['multiplicacao']#acessando a funçao lambda do id multiplicaçao no dic calculadora

print('A soma eh: {}'.format(soma(10,5)))
print('A multiplicaçao eh: {}'.format(multiplicacao(10,5)))


