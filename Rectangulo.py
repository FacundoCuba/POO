class Rectangulo():
    def __init__(self, may, men):
        self.ladoMayor = may
        self.ladoMenor = men
    def darPerimetro(self):
        return (self.ladoMayor*2) + (self.ladoMenor*2)

    def darSuperficie(self):
        return (self.ladoMayor*self.ladoMayor)


r1 = Rectangulo(2,2)
print(r1.darPerimetro())
print(r1.darSuperficie())