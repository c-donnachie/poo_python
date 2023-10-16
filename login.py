class Usuario:
    def __init__(self, usuario, email, password):
        self.usuario = usuario
        self.email = email
        self.password = password

    def validar_email(self, email):
        return email == self.email

    def validar_password(self, password):
        return password == self.password


class Estudiante(Usuario):
    def __init__(self, usuario, email, password, universidad, carrera):
        super().__init__(usuario, email, password)
        self.universidad = universidad
        self.carrera = carrera


usuario1 = Estudiante(
    "cristian", "ugar.cristian@gmail.com", "1234", "inacap", "ing software"
)


def obtener_email_valido():
    while True:
        email = input("Escribe tu email: ")
        if usuario1.validar_email(email):
            return email
        else:
            print("Email incorrecto. Inténtalo nuevamente.")


def obtener_password_valido():
    while True:
        password = input("Escribe tu password: ")
        if usuario1.validar_password(password):
            return password
        else:
            print("Password incorrecto. Inténtalo nuevamente.")


try:
    email = obtener_email_valido()
    password = obtener_password_valido()
    print("Inicio de sesión exitoso!")
except KeyboardInterrupt:
    print("\nProceso de inicio de sesión interrumpido.")
