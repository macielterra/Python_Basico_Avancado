class Calculadora:
    def __init__(self, num1, num2):
        #_init_: inicializa variaveis de atributos da classe qdo um obj for instaciado
        #self referencia o proprio objeto
        self.a = num1
        self.b = num2

    #self eh pra acessar os valores da classe   
    def soma(self):
        calc = self.a + self.b
        return calc

    def subtracao(self):
        calc = self.a - self.b
        return calc
        
    def multiplicacao(self):
       calc = self.a * self.b
       return calc

    def divisao(self):
        calc = self.a / self.b
        return calc

if __name__ == "__main__":
    
    calculadora = Calculadora(10,2)

    print(calculadora.a)
    print(calculadora.b)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())


