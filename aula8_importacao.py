from aula7_tv import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contadorLetras

if __name__ == "__main__":
    
    #Importaçao Classes
    tv = Televisao()#instanciado objeto
    print(tv.ligada)#print atributo
    tv.power()
    print(tv.ligada)#print atributo

    calcular = Calculadora(10,5)#instanciado objeto
    print(calcular.soma())#print retorno de um metodo

    #Importaçao de funçao
    lista = ['cachorro','gato','elefante']#parametro da funçao
    print(contadorLetras(lista))#print chamando a funçao e mandando o parametro que ela exige

