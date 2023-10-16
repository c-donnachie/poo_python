# Herencia Multiple


class Animal:
    def comer(self):
        print("Comiendo")


class Mamifero(Animal):
    def amamantar(self):
        print("Amantando")


class Ave(Animal):
    def volar(self):
        print("Volando")


class Murcielago(Mamifero, Ave):
    # def amamantar(self):
    #     super(Mamifero, self).amamantar()
    #     super(Ave, self).volar()
    pass


ave = Ave()
ave.comer()
# ave.amamantar()
ave.volar()
