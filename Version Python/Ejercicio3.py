import tkinter as tk
from tkinter import messagebox


# Clase base
class Vehiculo:
    def arrancar(self):
        print("El vehículo ha arrancado.")

    def detener(self):
        print("El vehículo se ha detenido.")


# Clase derivada
class Coche(Vehiculo):
    def conducir(self):
        print("El coche está siendo conducido.")


# Interfaz gráfica
class Aplicacion:
    def __init__(self, ventana):

        self.ventana = ventana

        # Configuración de la ventana
        self.ventana.title(
            "Ejercicio 3 - Herencia Simple"
        )

        self.ventana.geometry("500x500")
        self.ventana.resizable(False, False)

        # Crea una instancia de Coche y Coche hereda de Vehiculo
        self.coche = Coche()

        # Título
        titulo = tk.Label(
            ventana,
            text="EJERCICIO 3: HERENCIA SIMPLE",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=20)

        subtitulo = tk.Label(
            ventana,
            text="Control de un coche",
            font=("Arial", 12)
        )

        subtitulo.pack()

        tk.Label(
            ventana,
            text="-" * 50
        ).pack(pady=10)

        # Información
        tk.Label(
            ventana,
            text=(
                "Seleccione una acción para demostrar\n"
                "los métodos heredados y propios del coche."
            ),
            font=("Arial", 11),
            justify="center"
        ).pack(pady=15)

        # Botón arrancar
        tk.Button(
            ventana,
            text="Arrancar",
            width=25,
            command=self.arrancar
        ).pack(pady=8)

        # Botón conducir
        tk.Button(
            ventana,
            text="Conducir",
            width=25,
            command=self.conducir
        ).pack(pady=8)

        # Botón detener
        tk.Button(
            ventana,
            text="Detener",
            width=25,
            command=self.detener
        ).pack(pady=8)

        # Área del reultado
        self.resultado = tk.Label(
            ventana,
            text="Seleccione una acción.",
            font=("Arial", 12, "bold"),
            justify="center",
            wraplength=400
        )

        self.resultado.pack(pady=25)

        # Botón salir
        tk.Button(
            ventana,
            text="Salir",
            width=25,
            command=ventana.destroy
        ).pack(pady=5)

    # Métodos de la interfaz
    def arrancar(self):

        # Método heredado de Vehiculo
        self.coche.arrancar()

        self.resultado.config(
            text="El vehículo ha arrancado."
        )

    def conducir(self):

        # Método propio de Coche
        self.coche.conducir()

        self.resultado.config(
            text="El coche está siendo conducido."
        )

    def detener(self):

        # Método heredado de Vehiculo
        self.coche.detener()

        self.resultado.config(
            text="El vehículo se ha detenido."
        )

# Inicio de aplicación

ventana = tk.Tk()

app = Aplicacion(ventana)

ventana.mainloop()