import datetime

class Nota:
    def __init__(self):
        self.id = 0
        self.titulo = ""
        self.texto = ""
        self.fecha = ""

class Block:
    def __init__(self):
        self.notas = []
        self.prox_id = 0

    def agregar(self, nota):
        self.notas.append(nota)
        self.prox_id = self.prox_id + 1

    def modificar(self, id, nota):
        #todo

    def buscar(self, id):
        self.notas.index(id + 1)

    def borrar(self, id):
        self.notas.remove(id + 1)

class Menu:
    def __init__(self):
        self.miBlock = Block()
        self.funciones = {
            "1": self.listarNotas,
            "2": self.agregarNota,
            "3": self.modificarNota,
            "4": self.borrarNota,
            "5": self.buscarNota
        }

    def listarNotas(self):
        print("Listado de notas del block")
        for n in self.miBlock.notas:
            print("=" * 40)
            print(n.id, end=' - ')
            print(n.titulo, end=" - ")
            print(n.fecha)
            print(n.texto)
            print()

    def mostrarMenu(self):
        while True:
            print("Ingrese opción:")
            print("""
                1. Listar notas
                2. Agregar Nota
                3. Modificar Nota
                4. Borrar Nota
                5. Buscar Nota
                6. Salir
            """)
            opc = self.ingresarOpcion()
            if opc == 6:
                break
            else:
                funcion = self.funciones[opc]

                if funcion:
                    funcion()

    def ingresarOpcion(self):
        return input("ingrese opción >")

    def agregarNota(self):
        n = Nota()
        n.titulo = input("Ingrese título: ")
        n.texto = input("Ingrese texto: ")
        n.id = self.miBlock.prox_id
        n.fecha = datetime.datetime.today()
        self.miBlock.agregar(n)

    def borrarNota(self):
        id = input("Ingrese el id de la nota a borrar: ")
        self.miBlock.borrar(id)

    def modificarNota(self):
        id = input("Ingrese el id de la nota a modificar: ")
        self.miBlock.modificar(id,n)
        #todo

    def buscarNota(self):
        id = input("Ingrese el id de la nota a buscar: ")
        self.miBlock.buscar(id)

if __name__ == '__main__':
    mnu = Menu()
    mnu.mostrarMenu()
