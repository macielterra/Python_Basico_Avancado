class Calculadora:
 
    #self eh pra acessar os valores da classe   
    def soma(self, a, b):
        calc = a+b
        return calc

    def subtracao(self, a, b):
        calc = a-b
        return calc
        
    def multiplicacao(self, a, b):
       calc = a*b
       return calc

    def divisao(self, a, b):
        calc = a/b
        return calc
        
if __name__ == "__main__":
    
    calculadora = Calculadora()

    print(calculadora.soma(10,2))
    print(calculadora.subtracao(10,2))
    print(calculadora.multiplicacao(10,2))
    print(calculadora.divisao(10,2))


