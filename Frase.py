class Frase():
    def __init__(self):
        self.texto = ""
    def darVocales(self):
        vocales = []
        for l in self.texto:
            if l in "aeiou":
                vocales.append(l)
        return vocales

    def darLargo(self):
        return len(self.texto)

frase = Frase()
frase.texto = "la vaca"
print(frase.darVocales())
print(frase.darLargo())