class Persona():
    def __init__(self, nom, doc):
        self.nombre = nom
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

class Visor():
    def __init__(self):
        pass

    def mostrarCola(self):
        print("Nombre", end=" ")
        print("DNI", end=" ")
        print("Turno")
        for p in cola.pers:
            print(p.nombre, end=" ")
            print(p.dni, end=" ")
            print(p.numAsignado)

    def buscarPersona(self, p):
        for i in cola.pers:
            if p in i.nombre:
                print(i.nombre, end=" ")
                print(i.dni, end=" ")
                print(i.numAsignado)
            elif p in i.dni:
                print(i.nombre, end=" ")
                print(i.dni, end=" ")
                print(i.numAsignado)

cola = ColaEspera(3)
for i in range(2):
    n = input("Ingrese su nombre: ")
    d = input("Ingrese su numero de DNI: ")
    turno = cola.agregar(Persona(n, d))
    print("Bienvenido", n, "su turno es:", turno)

ver = Visor()
print("")
ver.mostrarCola()
print("")
ver.buscarPersona(str(111))

"""""
for i in cola.pers:
    print(i.nombre, end=" ")
    print(i.dni, end=" ")
    print(i.numAsignado)

print("El siguiente es:", cola.atenderProx())

for i in cola.pers:
    print(i.nombre, end=" ")
    print(i.dni, end=" ")
    print(i.numAsignado)
"""