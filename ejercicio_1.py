class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_nombre(self):
        print(f"Nombre: {self.nombre}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def imprimir_grado(self):
        print(f"Grado: {self.grado}")


cristian = Estudiante("Cristian", 24, 2)


cristian.imprimir_nombre()
