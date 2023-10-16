# Metodo de resolucion de orden
# Pririzando como un arbol de ramas


class A:
    def hablar(self):
        print("Hola desde A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()

d.hablar()


print(D.mro())
