class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido.")


class Mamifero(Animal):
    def alimentar(self):
        print("El mamífero se está alimentando.")


class Perro(Mamifero):
    def hacer_sonido(self):
        print("El perro hace el sonido: ¡Guau!")


def main():
    perro = Perro()

    print("Validando herencia multinivel y sobreescritura de metodos")

    perro.hacer_sonido()
    perro.alimentar()


if __name__ == "__main__":
    main()