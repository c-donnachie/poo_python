class Persona:
    def __init__(self, nombre, país):
        self.nombre = nombre
        self.país = país

    def idenCompleto(self):
        print(f"Hola, soy {self.nombre}, mi país de origen es {self.país}")


class Canal:
    ncanales = 0

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        Canal.ncanales += 1

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    @classmethod
    def demonetizar(cls, n):
        if Canal.ncanales - n >= 0:
            Canal.ncanales -= n
        else:
            print("No se puede demonetizar más canales que los disponibles.")


class Suscriptor(Persona):
    def __init__(self, nombre, país, nombreUsuario):
        super().__init__(nombre, país)
        self.suscripciones = []
        self.nombreUsuario = nombreUsuario

    def setNombreUsuario(self, nombreUsuario):
        self.nombreUsuario = nombreUsuario

    def getNombreUsuario(self):
        return self.nombreUsuario

    def agregarSuscripcion(self, canal):
        self.suscripciones.append(canal)

    def listarSuscripciones(self):
        print("Canales a los que está suscrito:")
        for canal in self.suscripciones:
            print(canal.getNombre())

    def idenCompleto(self):
        print(
            f"Hola, soy {self.nombre}, mi nombre de usuario es {self.nombreUsuario} y mi país de origen es {self.país}"
        )


class Youtuber(Suscriptor):
    def __init__(self, nombre, país, nombreUsuario, nombreC, tipo):
        super().__init__(nombre, país, nombreUsuario)
        self.canalP = Canal(nombreC, tipo)

    def setCanalP(self, nombreC, tipo):
        self.canalP = Canal(nombreC, tipo)

    def getCanalP(self):
        return self.canalP

    def idenCompleto(self):
        print(
            f"Hola, soy {self.nombre}, mi nombre de usuario es {self.nombreUsuario} y soy youtuber!!!"
        )


c1 = Canal("Mala Leche", "humor")
c2 = Canal("Cocina Misteriosa", "Cocina")
y1 = Youtuber("Enrique", "Chile", "El Enri", "Entrenando con Enri", "deporte")
y2 = Youtuber("Alice", "Dinamarca", "Alicia", "Alicia in Wonderland", "misc")
s1 = Suscriptor("Teresa", "Mexico", "Tere")
s2 = Suscriptor("Asuka", "Japón", "Aska")
y1.idenCompleto()
y2.idenCompleto()
s1.idenCompleto()
s2.idenCompleto()
s1.agregarSus(c1)
s1.agregarSus(y1.getcanalP())
s1.agregarSus(y2.getcanalP())
s2.agregarSus(c1)
s2.agregarSus(y2.getcanalP())
s2.agregarSus(c2)
print()
s1.listarSus()
print()
s2.listarSus()
print()
print(Canal.ncanales)
Canal.demonetizar(1)
print(Canal.ncanales)
print()
print(y1._Youtuber__canalP.getnombre())
print(y2._Youtuber__canalP.getnombre())
