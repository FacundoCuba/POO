import time
import random

jardin = {}

class Planta():
    def __init__(self):
        self.luz = 0
        self.agua = 0
        self.nutrientes = 0

    def ambienteInicial(self):
        total = self.luz + self.agua + self.nutrientes
        return total

    def condicion(self):
        if self.ambienteInicial() + random.choice([-30,-20,-10,0,10,20,30]) <= 0:
            return "muerta"
        elif self.ambienteInicial() + random.choice([-30,-20,-10,0,10,20,30]) > 0 and self.ambienteInicial() + random.choice([-30,-20,-10,0,10,20,30]) < 10:
            return "sobreviviendo"
        elif self.ambienteInicial() + random.choice([-30,-20,-10,0,10,20,30]) >= 10 and self.ambienteInicial() + random.choice([-30,-20,-10,0,10,20,30]) < 100:
            return "creciendo"
        elif self.ambienteInicial() + random.choice([-30,-20,-10,0,10,20,30]) >= 100:
            return "reproductiva"


girasol = Planta()
girasol.luz = -10
girasol.agua = -10
girasol.nutrientes = -10

rosa = Planta()
rosa.luz = -10
rosa.agua = -10
rosa.nutrientes = -10

tomate = Planta()
tomate.luz = -10
tomate.agua = -10
tomate.nutrientes = -10

lechuga = Planta()
lechuga.luz = -10
lechuga.agua = -10
lechuga.nutrientes = -10

zanahoria = Planta()
zanahoria.luz = -10
zanahoria.agua = -10
zanahoria.nutrientes = -10

while True:
    jardin['girasol'] = girasol.condicion()
    jardin['rosa'] = rosa.condicion()
    jardin['tomate'] = tomate.condicion()
    jardin['lechuga'] = lechuga.condicion()
    jardin['zanahoria'] = zanahoria.condicion()
    print("")
    print("*")
    print(jardin)
    time.sleep(3)

