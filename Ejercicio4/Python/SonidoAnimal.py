class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido.")


class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace el sonido: ¡Guau!")


class Gato(Animal):
    def hacer_sonido(self):
        print("El gato hace el sonido: ¡Miau!")


def main():
    animal = None
    opcion = ""

    while opcion != "3":
        print("\n* Selección de Animal *")
        print("1. Perro")
        print("2. Gato")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            animal = Perro()
            animal.hacer_sonido()

        elif opcion == "2":
            animal = Gato()
            animal.hacer_sonido()

        elif opcion == "3":
            print("Programa finalizado.")

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
