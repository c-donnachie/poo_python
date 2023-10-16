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
