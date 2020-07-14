#Para criar uma classe error personalizada eh  preciso sempre criar uma classe que herde Exception
#mesmo que ela fique vazia

class Error(Exception):
    pass

class InputError(Error):#herança - InputError herda de Error
    def __init__(self, message):
        self.message = message


while True:#Sempre executa sem fim
    try:
        x = int(input('Entre com uma nota: '))
        print(x)
        if x > 10:
            #Forçando exceçao
            raise InputError('Nota nao pode ser maior que 10')
        elif x<0:
            raise InputError('Nota nao pode ser menor que 0')

        break #força a saida do loop quando ele entrar com valor correto
    
    except ValueError:
        print('Valor Invalido. Deve-se digitar apenas numero')
    except InputError as ex:
        print(ex)
