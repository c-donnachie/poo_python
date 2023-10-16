class Gato:
    def sonido(self):
        return "Miau"


class Perro:
    def sonido(self):
        return "Guau"


def hacer_Sonido(animal):
    print(animal.sonido())


gato = Gato()
perro = Perro()

# Polimorfismo con diferente argumento de la funcion.
# Mismo metodo, funciona diderente para diferentes argumentos
hacer_Sonido(perro)

# Polimorfismo mismo metodo, con diferente objeto
# Cambia el objeto para el metodo
print(gato.sonido())


# Polimorfismo de herencia, subtipos o subclases
