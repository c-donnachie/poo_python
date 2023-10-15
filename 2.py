class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estas haciendo un llamado {self.modelo}")

    def cortar(self):
        print(f"Cortaste la llamada de {self.modelo}")


Celular1 = Celular("Samsung", "s23 Ultra", "48MP")
Celular2 = Celular("Apple", "iPhone 15 Pro", "98MP")

Celular2.llamar()

# Metodos, los metodos son basicamente funciones pero dentro de nuestra clase/objeto


class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = (nombre,)
        self.email = (email,)
        self.password = password

    def decirUsuario(self):
        print(f"MI usuario es {self.nombre}")


usuario1 = Usuario("cristian", "ugar.cristian@gmail.com", "123")

usuario1.decirUsuario()


class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = (codigo,)
        self.__nombre = (nombre,)
        self.__precio = precio

    # Getter
    @property
    def codigo(self):
        return self.__codigo

    # Setter
    @codigo.setter
    def codigo(self, valor):
        self.codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.nombre = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        self.precio = valor

    def __str__(self):
        return (
            "codigo:" + str(self.__codigo) + "nombre:",
            str(self.__nombre),
            "codigo:" + str(self.__codigo),
        )


p1 = Producto(1, "Cargador", 3990)
p2 = Producto(2, "Cable tipo c", 4990)

print(p1)
print(p2)
