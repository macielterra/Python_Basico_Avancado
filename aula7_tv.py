#Liga e desliga Tv e muda de canal se ela estiver ligada

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    
    def power(self):
        if self.ligada:#padrao ele ja considera como True
            self.ligada = False
        else:
            self.ligada = True

    def aumentaCanal(self):
        if self.ligada:
            self.canal += 1

    def voltaCanal(self):
        if self.ligada:
            self.canal -= 1

print(__name__)
##serve para teste, se esquecer parte de codigo instanciando ele no roda esse bloco se for de importaçao
if __name__ == "__main__":
    
    tv = Televisao()
    print('TV esta ligada?: {}'.format(tv.ligada))

    tv.power()
    print('TV esta ligada?: {}'.format(tv.ligada))
    print('Canal: {}'.format(tv.canal))
    tv.aumentaCanal()
    print('Canal: {}'.format(tv.canal))
    tv.aumentaCanal()
    tv.aumentaCanal()
    print('Canal: {}'.format(tv.canal))
    tv.voltaCanal()
    print('Canal: {}'.format(tv.canal))
    tv.power()
    print('TV esta ligada?: {}'.format(tv.ligada))

