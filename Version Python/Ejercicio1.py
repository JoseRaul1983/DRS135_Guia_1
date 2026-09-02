import tkinter as tk
from tkinter import messagebox

# Clase que representa la abstracción
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        # El saldo se mantiene como un detalle interno de la clase.
        self._saldo = saldo_inicial

    def depositar(self, monto):
        if monto <= 0:
            return False

        self._saldo += monto
        return True

    def retirar(self, monto):
        if monto <= 0:
            return False

        if monto > self._saldo:
            return False

        self._saldo -= monto
        return True

    def consultar_saldo(self):
        return self._saldo

# Configuración de interfaz gráfica
class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana

        self.ventana.title("Ejercicio 1 - Abstracción")
        self.ventana.geometry("500x450")
        self.ventana.resizable(False, False)

        # Crear una cuenta bancaria
        self.cuenta = CuentaBancaria(0)

        # Título de ventana
        titulo = tk.Label(
            ventana,
            text="EJERCICIO 1: ABSTRACCIÓN",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=20)

        subtitulo = tk.Label(
            ventana,
            text="Cuenta bancaria",
            font=("Arial", 12)
        )
        subtitulo.pack()

        # Separador visual
        tk.Label(
            ventana,
            text="-" * 50
        ).pack(pady=10)

        # Campo para ingresar monto
        tk.Label(
            ventana,
            text="Ingrese el monto:"
        ).pack(pady=5)

        self.entrada_monto = tk.Entry(
            ventana,
            width=25,
            justify="center"
        )
        self.entrada_monto.pack()

        # Botones
        tk.Button(
            ventana,
            text="Depositar",
            width=20,
            command=self.depositar
        ).pack(pady=10)

        tk.Button(
            ventana,
            text="Retirar",
            width=20,
            command=self.retirar
        ).pack(pady=5)

        tk.Button(
            ventana,
            text="Consultar saldo",
            width=20,
            command=self.consultar_saldo
        ).pack(pady=5)

        # Área para mostrar resultados
        self.resultado = tk.Label(
            ventana,
            text="Saldo actual: $0.00",
            font=("Arial", 13, "bold")
        )
        self.resultado.pack(pady=25)

        # Botón salir
        tk.Button(
            ventana,
            text="Salir",
            width=20,
            command=ventana.destroy
        ).pack(pady=5)

    # MÉTODOS DE LA INTERFAZ
    
    def obtener_monto(self):
        try:
            monto = float(self.entrada_monto.get())

            if monto <= 0:
                messagebox.showerror(
                    "Error",
                    "El monto debe ser mayor que 0."
                )
                return None

            return monto

        except ValueError:
            messagebox.showerror(
                "Error",
                "Debe ingresar un monto numérico válido."
            )
            return None

    def depositar(self):
        monto = self.obtener_monto()

        if monto is None:
            return

        if self.cuenta.depositar(monto):
            self.actualizar_saldo()

            messagebox.showinfo(
                "Depósito",
                f"Se depositaron ${monto:.2f} correctamente."
            )

    def retirar(self):
        monto = self.obtener_monto()

        if monto is None:
            return

        if monto > self.cuenta.consultar_saldo():
            messagebox.showerror(
                "Error",
                "No hay suficiente saldo para realizar el retiro."
            )
            return

        if self.cuenta.retirar(monto):
            self.actualizar_saldo()

            messagebox.showinfo(
                "Retiro",
                f"Se retiraron ${monto:.2f} correctamente."
            )

    def consultar_saldo(self):
        saldo = self.cuenta.consultar_saldo()

        messagebox.showinfo(
            "Saldo",
            f"El saldo actual es: ${saldo:.2f}"
        )

        self.actualizar_saldo()

    def actualizar_saldo(self):
        saldo = self.cuenta.consultar_saldo()

        self.resultado.config(
            text=f"Saldo actual: ${saldo:.2f}"
        )


# Inicio de la aplicación

ventana = tk.Tk()

app = Aplicacion(ventana)

ventana.mainloop()