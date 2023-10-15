class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")


nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
grado = int(input("Escribe tu grado: "))

estudiante = Estudiante(nombre, edad, grado)

print(
    f"""DATOS DEL ESTUDIANTE: \n\n
Nombre: {estudiante.nombre} \n
Edad: {estudiante.edad} \n
Grado: {estudiante. grado} \n
      """
)

while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()
    elif estudiar == "0":
        break
