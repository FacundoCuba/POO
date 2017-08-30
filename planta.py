import time

class Planta():
    def __init__(self):
        self.luz = 0
        self.agua = 0
        self.nutrientes = 0

    def ambienteInicial(self):
        total = self.luz + self.agua + self.nutrientes
        return total

    def condicion(self):
        if self.ambienteInicial() <= 0:
            return "muerta"
        elif self.ambienteInicial() > 0 and self.ambienteInicial() < 10:
            return "sobreviviendo"
        elif self.ambienteInicial() >= 10 and self.ambienteInicial() < 100:
            return "creciendo"
        elif self.ambienteInicial() >= 100:
            return "reproductiva"

girasol = Planta()
girasol.luz = 0
girasol.agua = 0
girasol.nutrientes = 101
while True:
    print("*")
    print(girasol.condicion())
    time.sleep(3)

