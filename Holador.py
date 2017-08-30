class Holador:
    saludos = {"es": "hola", "en": "hello", "de": "hallo", "da": "hej", "it": "ciao", "fr": "salut", "pt": "Olá"}
    poblacion = 0

    def __init__(self, nom, nac):
        self.nombre = nom
        self.nacionalidad = nac

        if nac in Holador.saludos.keys():
            self.saludo = Holador.saludos[nac]
        else:
            self.saludo = "Hi"

        Holador.poblacion = Holador.poblacion + 1

    def saludar(self):
        return self.saludo + "!"

def main(args):
    p1 = Holador("Simona", "it")
    p1.saludar()
    p2 = Holador("Rolf", "de")
    p3 = Holador("Pilar", "es")
    p4 = Holador("Diego", "es")

    holadores = []
    holadores.append(p1)
    holadores.append(p2)
    holadores.append(p3)

    print(Holador.poblacion)

    holadores.append(p4)
    holadores.append(Holador("Olaf", "da"))
    holadores.append(Holador("Peter", "en"))

    print(Holador.poblacion)

    holadores.append(Holador("Toto", "argentina"))

    for p in holadores:
        print(p.nombre + ": - " + p.saludo + "!")

    print(Holador.poblacion)

    return 0

if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))