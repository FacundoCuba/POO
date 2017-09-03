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
girasol.luz = 0
girasol.agua = 0
girasol.nutrientes = 0

rosa = Planta()
rosa.luz = 0
rosa.agua = 0
rosa.nutrientes = 0

tomate = Planta()
tomate.luz = 0
tomate.agua = 0
tomate.nutrientes = 0

lechuga = Planta()
lechuga.luz = 0
lechuga.agua = 0
lechuga.nutrientes = 0

zanahoria = Planta()
zanahoria.luz = 0
zanahoria.agua = 0
zanahoria.nutrientes = 0

while True:
    jardin['girasol'] = girasol.condicion()
    jardin['rosa'] = rosa.condicion()
    jardin['tomate'] = tomate.condicion()
    jardin['lechuga'] = lechuga.condicion()
    jardin['zanahoria'] = zanahoria.condicion()
    stop = {"p1":"muerta", "p2":"muerta", "p3":"muerta", "p4":"muerta","p5":"muerta"}
    if all(v == "muerta" for v in jardin.values()):
        exit()

    print("")
    print("*")
    print(jardin)
    time.sleep(3)

