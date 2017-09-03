class Persona():
    def __init__(self, nom, doc):
        self.nompre = nom
        self.dni = doc
        self.numeroAsignado = 0

    def darNum(self):
        return self.numeroAsignado


class ColaEspera():
    def __init__(self, n):
        self.pers = []
        self.cantEnCola = 0
        self.proxNum = n

    def agregar(self, p):
        p.numAsignado = self.proxNum
        self.pers.append(p)
        aux = p.numAsignado
        self.proxNum = self.proxNum + 1
        return aux

    def atenderProx(self):
        p = self.pers.pop(0)
        return p.numAsignado

cola = ColaEspera(3)
n = input("Ingrese su nombre: ")
d = input("Ingrese su numero de DNI: ")
print(cola.agregar(Persona(n, d)))


