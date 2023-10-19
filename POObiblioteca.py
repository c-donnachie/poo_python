# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:50:30 2022

@author: Victor Valenzuela
"""


class Documento:
    def __init__(self, estado, iden, nombre, desc, tema):
        self.estado = estado
        self.iden = iden
        self.nombre = nombre
        self.desc = desc
        self.tema = tema

    def getestado(self):
        return self.estado

    def getiden(self):
        return self.iden

    def getnombre(self):
        return self.nombre

    def getdesc(self):
        return self.desc

    def gettema(self):
        return self.tema

    def setestado(self, estado):
        self.estado = estado

    def setiden(self, iden):
        self.iden = iden

    def setnombre(self, nombre):
        self.nombre = nombre

    def setdesc(self, desc):
        self.desc = desc

    def settema(self, tema):
        self.tema = tema


class Libro(Documento):
    def __init__(self, estado, iden, nombre, desc, tema, autor):
        self.autor = autor
        super().__init__(estado, iden, nombre, desc, tema)

    def getautor(self):
        return self.autor

    def setautor(self, autor):
        self.autor = autor


class Revista(Documento):
    def __init__(self, estado, iden, nombre, desc, tema, numero):
        self.numero = numero
        super().__init__(estado, iden, nombre, desc, tema)

    def getnumero(self):
        return self.numero

    def setnumero(self, numero):
        self.numero = numero


class Estante:
    def __init__(self, iden, tema, documentos):
        self.documentos = documentos  # se pide el arreglo de documentos por parametro
        # también se podría empezar con un arreglo vacío y crear un metodo que agregue libros
        # a ese arreglo
        # self.documentos = [] #sería para dejar un arreglo vacío en el estante como base
        self.iden = iden
        self.tema = tema

    # método que podría agregar documentos al arreglo
    def agregardocs(self, doc):
        self.getdocs().append(doc)

    def getdocs(self):
        return self.documentos

    def setdocs(self, docs):
        self.documentos = docs

    def listarDocumentos(self):
        a = self.getdocs()
        ix = 0  # indice
        for i in a:
            print("indice:", ix, "nombre:", i.getnombre(), "prestado?:", i.getestado())
            ix += 1

    def prestarDocumento(self, n):
        if self.getdocs()[n].getestado() == 1:
            self.documentos[n].setestado(0)  # prestado
        else:
            print("el libro ya está prestado...")

    def regresarDocumento(self, n):
        if self.getdocs()[n].getestado() == 0:
            self.documentos[n].setestado(1)  # regresa
        else:
            print("el libro ya existe...")


a = Libro(
    1,
    33,
    "libro de la vida",
    "un libro que explica la vida",
    "filosofía",
    "intro...etc",
)
b = Libro(
    1,
    105,
    "libro de la muerte",
    "un libro que explica la muerte",
    "filosofía",
    "intro...etc",
)
c = Libro(
    1,
    355,
    "libro de la biología",
    "un libro que habla de biología básica",
    "biología",
    "intro...etc",
)
d = Libro(1, 6, "matemáticas", "intro a las matemáricas", "matemáticas", "intro...etc")
e = Revista(1, 3377, "Revista Life", "revista sobre estilo de vida", "social", 10)
f = Revista(1, 665, "Revista Club Nintendo", "revista sobre videojuegos", "juegos", 17)
g = Revista(1, 234, "Revista Club Nintendo", "revista sobre videojuegos", "juegos", 34)
h = Revista(1, 97654, "Revista Barrabases", "revista sobre humor y futbol", "humor", 8)

est = Estante(1, "misc", [a, b, c, d, e, f, g, h])
est.listarDocumentos()
est.prestarDocumento(0)
est.listarDocumentos()
est.regresarDocumento(0)
est.listarDocumentos()
est.agregardocs(Revista(1, 10, "Revista Tipo", "revista sobre nada", "existencia", 1))
est.listarDocumentos()


class Canal:
    def __init__(self, nombreC, tipo):
        self.nombreC = nombreC
        self.tipo = tipo


class Suscriptor:
    def __init__(self, nombre, país, nombreUsuario):
        self.nombre = nombre
        self.país = país
        self.nombreUsuario = nombreUsuario

    def idenCompleto(self):
        print(
            f"Hola, soy {self.nombre}, mi nombre de usuario es {self.nombreUsuario} y soy suscriptor!!!"
        )


class Youtuber(Suscriptor):
    def __init__(self, nombre, país, nombreUsuario, nombreC, tipo):
        super().__init__(nombre, país, nombreUsuario)
        self.canalP = Canal(nombreC, tipo)

    def setcanalP(self, nombreC, tipo):
        self.canalP = Canal(nombreC, tipo)

    def getcanalP(self):
        return self.canalP

    def idenCompleto(self):
        print(
            f"Hola, soy {self.nombre}, mi nombre de usuario es {self.nombreUsuario} y soy youtuber!!!"
        )


# Ejemplo de uso:
youtuber1 = Youtuber(
    "Esteban", "Argentina", "Estebo", "Canal de Estebo", "Entretenimiento"
)
print("Nombre del canal personal:", youtuber1.getcanalP().nombreC)
print("Tipo de canal personal:", youtuber1.getcanalP().tipo)
youtuber1.idenCompleto()
