import tkinter as tk
from tkinter import messagebox

# Clase base
class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido.")
        return "El animal hace un sonido."

# Clase intermedia
class Mamifero(Animal):

    def alimentar(self):
        print("El mamífero se está alimentando.")
        return "El mamífero se está alimentando."

# Clase derivada
class Perro(Mamifero):

    def hacer_sonido(self):
        print("El perro hace el sonido: ¡Guau!")
        return "El perro hace el sonido: ¡Guau!"

# Interfaz gráfica
class Aplicacion:

    def __init__(self, ventana):

        self.ventana = ventana

        # Configuración de la ventana
        self.ventana.title(
            "Ejercicio 5 - Herencia Multinivel"
        )

        self.ventana.geometry("600x650")
        self.ventana.resizable(False, False)

        # Se crea una instancia de Perro, Perro hereda de Mamifero y Mamifero hereda de Animal.
        self.perro = Perro()

        # Título
        titulo = tk.Label(
            ventana,
            text="EJERCICIO 5: HERENCIA MULTINIVEL",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=20)

        subtitulo = tk.Label(
            ventana,
            text="Herencia y sobrescritura de métodos",
            font=("Arial", 12)
        )

        subtitulo.pack()

        tk.Label(
            ventana,
            text="-" * 60
        ).pack(pady=10)

        # Jerarquía de clases
        tk.Label(
            ventana,
            text="Jerarquía de clases:",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        tk.Label(
            ventana,
            text=(
                "Animal\n"
                "   ↓\n"
                "Mamifero\n"
                "   ↓\n"
                "Perro"
            ),
            font=("Arial", 11),
            justify="center"
        ).pack(pady=5)

        # Botón "hacer sonido"
        tk.Button(
            ventana,
            text="Hacer sonido",
            width=30,
            command=self.hacer_sonido
        ).pack(pady=8)

        # Botón "alimentar"
        tk.Button(
            ventana,
            text="Alimentar",
            width=30,
            command=self.alimentar
        ).pack(pady=8)

        # Botón "demostrar herencia"
        tk.Button(
            ventana,
            text="Demostrar toda la herencia",
            width=30,
            command=self.demostrar_herencia
        ).pack(pady=8)

        # Área del ressultado
        tk.Label(
            ventana,
            text="Resultado:",
            font=("Arial", 12, "bold")
        ).pack(pady=(20, 5))

        self.resultado = tk.Label(
            ventana,
            text="Seleccione una opción.",
            font=("Arial", 11),
            justify="center",
            wraplength=520
        )

        self.resultado.pack(pady=10)

        # Botón "limpiar"
        tk.Button(
            ventana,
            text="Limpiar",
            width=30,
            command=self.limpiar
        ).pack(pady=5)

        # Botón "salir"
        tk.Button(
            ventana,
            text="Salir",
            width=30,
            command=ventana.destroy
        ).pack(pady=5)

    # Método "hacer sonido"
    def hacer_sonido(self):

        # Perro sobreescribe el método
        # hacer_sonido() definido originalmente
        # en Animal.
        resultado = self.perro.hacer_sonido()

        self.resultado.config(
            text=(
                "Método sobreescrito:\n\n"
                f"{resultado}\n\n"
                "Perro ha sobrescrito el método "
                "hacer_sonido() de Animal."
            )
        )

    # Método "alimentar"
    def alimentar(self):

        # Este método pertenece a Mamifero
        # y es heredado por Perro.
        resultado = self.perro.alimentar()

        self.resultado.config(
            text=(
                "Método heredado:\n\n"
                f"{resultado}\n\n"
                "Perro hereda el método alimentar() "
                "de Mamifero."
            )
        )

    # Demostración de la herencia
    def demostrar_herencia(self):

        sonido = self.perro.hacer_sonido()
        alimentacion = self.perro.alimentar()

        resultado = (
            "DEMOSTRACIÓN DE LA HERENCIA MULTINIVEL\n\n"
            "1. Animal\n"
            "   Define el método hacer_sonido().\n\n"
            "2. Mamifero\n"
            "   Hereda de Animal y añade alimentar().\n\n"
            "3. Perro\n"
            "   Hereda de Mamifero y sobrescribe "
            "hacer_sonido().\n\n"
            "RESULTADOS:\n\n"
            f"{sonido}\n"
            f"{alimentacion}"
        )

        self.resultado.config(
            text=resultado
        )

        messagebox.showinfo(
            "Demostración completada",
            "Se ejecutaron los métodos heredados "
            "y sobreescritos correctamente."
        )

    # Limpiar
    def limpiar(self):

        self.resultado.config(
            text="Seleccione una opción."
        )

# Inicio de aplicación

ventana = tk.Tk()

app = Aplicacion(ventana)

ventana.mainloop()