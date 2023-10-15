class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Estoy hablando un poco")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_Habilidad(self):
        print(f"Mi habilidad es {self.habilidad}")


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empleado = empresa

    def presentarme(self):
        return super().mostrar_Habilidad()


roberto = Persona("Roberto", 22, "chilena", "Cantar", 399000, "tecnobox")

# roberto.mostrar_Habilidad()


herencia = issubclass(EmpleadoArtista, Artista)
instancia = isinstance(roberto, Persona)

print(herencia)
