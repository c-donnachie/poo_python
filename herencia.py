class Usuario:
    def __init__(self, usuario, email, password):
        self.usuario = usuario
        self.email = email
        self.password = password


class Estudiante(Usuario):
    def __init__(self, usuario, email, password, univercidad, carrera):
        super().__init__(usuario, email, password)
        self.univercidad = univercidad
        self.carrera = carrera


cristian = Estudiante(
    "cristian", "ugar.cristian@gmail.com", "1234", "inacap", "ing software"
)

print(cristian.univercidad)
