# Podemos definir atributos y metodos privados incluyendo un _
# Esto lo convierte en "privado", pero igual se puede acceder a ellos,
# Y con __ se ocultan totalmente (py untenranamente re nombra el elemneto para
# que no se pueda acceder a el.)

# Y con el Getter and Sette, que no son mas que funciones o una conveccion
# que accede o modifica a un atrubuto o metodo.


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre


cristian = Persona("Cristian", 21)

nombre = cristian.get_nombre()
print(nombre)

cristian.set_nombre("Alejandro")

nombre = cristian.get_nombre()
print(nombre)
