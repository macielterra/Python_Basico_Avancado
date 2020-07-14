#tratamento de exceçao
lista = [1, 10]
try:
    divisao = 10/1
    numero = lista[1]
    #x = a

except ZeroDivisionError:
    print('Nao eh possivel realizar divisao por zero')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
#Tratando erros nao previstos
#except BaseException as ex:
 #   print('Erro nao previsto. Erro: {}'.format(ex))
except Exception as erro:
    print('Erro: {}'.format(erro))
else:#pode jogar trecho de codigo que nao pode haver nenhum erro previsto
    print('Executa quando nao ocorre exceçao')
finally:#pode usar em trechos d ecodigos que precisam ser executados independete de haver exceçoes ou nao
    print('Sempre executa independente de exceçao ou nao')