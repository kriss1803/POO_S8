# programa_poo.py

class Animal:
    """
    Clase base: Animal
    Esta clase representa un animal genérico.
    """

    def __init__(self, nombre, edad):
        # Encapsulamos los atributos con doble guion bajo para hacerlos privados
        self.__nombre = nombre
        self.__edad = edad

    # Getters y Setters para encapsulación
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("Edad inválida")

    def hacer_sonido(self):
        """
        Método genérico para que el animal haga un sonido.
        Será sobrescrito en las clases derivadas.
        """
        print("Este animal hace un sonido")

    def descripcion(self):
        """
        Método para mostrar información del animal.
        """
        print(f"Animal: {self.__nombre}, Edad: {self.__edad} años")


class Perro(Animal):
    """
    Clase derivada: Perro
    Hereda de Animal y sobrescribe métodos para demostrar polimorfismo.
    """

    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.__raza = raza  # atributo encapsulado

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def hacer_sonido(self):
        """
        Método sobrescrito: el perro hace un sonido específico.
        """
        print("Guau guau!")

    # Método polimórfico con argumento opcional
    def descripcion(self, mostrar_raza=False):
        """
        Sobrescribe la descripción para agregar la raza del perro opcionalmente.
        """
        super().descripcion()
        if mostrar_raza:
            print(f"Raza: {self.__raza}")


def main():
    # Crear una instancia de Animal
    animal = Animal("Animal Genérico", 5)
    animal.descripcion()
    animal.hacer_sonido()
    print("---")

    # Crear una instancia de Perro
    perro = Perro("Horus", 3, "Pitbull")
    perro.descripcion()
    perro.hacer_sonido()
    print("---")

    # Usar el método con polimorfismo pasando argumento
    perro.descripcion(mostrar_raza=True)
    print("---")

    # Probar encapsulación - acceso indirecto a atributos privados
    print(f"Nombre original del perro: {perro.get_nombre()}")
    perro.set_nombre("Rex")
    print(f"Nombre modificado del perro: {perro.get_nombre()}")

    print(f"Edad original del perro: {perro.get_edad()}")
    perro.set_edad(4)
    print(f"Edad modificada del perro: {perro.get_edad()}")

    # Intentar poner una edad inválida
    perro.set_edad(-1)


if __name__ == "__main__":
    main()
