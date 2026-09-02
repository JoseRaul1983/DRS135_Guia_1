import tkinter as tk
from tkinter import messagebox


# ==========================================
# CLASE EMPLEADO
# ==========================================

class Empleado:
    def __init__(self):
        # Atributos privados
        self._nombre = ""
        self._edad = 0

    # ======================================
    # PROPIEDAD NOMBRE
    # ======================================

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    # ======================================
    # PROPIEDAD EDAD CON VALIDACIÓN
    # ======================================

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        # La validación pertenece a la clase,
        # no a la interfaz gráfica.
        if valor > 0 and valor < 100:
            self._edad = valor
        else:
            raise ValueError(
                "La edad debe ser mayor que 0 y menor que 100."
            )


# ==========================================
# INTERFAZ GRÁFICA
# ==========================================

class Aplicacion:
    def __init__(self, ventana):

        self.ventana = ventana

        self.ventana.title(
            "Ejercicio 2 - Encapsulación"
        )

        self.ventana.geometry("500x500")
        self.ventana.resizable(False, False)

        # Crear objeto Empleado
        self.empleado = Empleado()

        # ==================================
        # TÍTULO
        # ==================================

        titulo = tk.Label(
            ventana,
            text="EJERCICIO 2: ENCAPSULACIÓN",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=20)

        subtitulo = tk.Label(
            ventana,
            text="Registro de empleado",
            font=("Arial", 12)
        )

        subtitulo.pack()

        tk.Label(
            ventana,
            text="-" * 50
        ).pack(pady=10)

        # ==================================
        # NOMBRE
        # ==================================

        tk.Label(
            ventana,
            text="Nombre del empleado:"
        ).pack(pady=5)

        self.entrada_nombre = tk.Entry(
            ventana,
            width=35
        )

        self.entrada_nombre.pack()

        # ==================================
        # EDAD
        # ==================================

        tk.Label(
            ventana,
            text="Edad del empleado:"
        ).pack(pady=10)

        self.entrada_edad = tk.Entry(
            ventana,
            width=35
        )

        self.entrada_edad.pack()

        # ==================================
        # BOTÓN REGISTRAR
        # ==================================

        tk.Button(
            ventana,
            text="Registrar empleado",
            width=25,
            command=self.registrar_empleado
        ).pack(pady=20)

        # ==================================
        # RESULTADO
        # ==================================

        self.resultado = tk.Label(
            ventana,
            text="Ingrese los datos del empleado.",
            font=("Arial", 12),
            justify="center"
        )

        self.resultado.pack(pady=20)

        # ==================================
        # BOTÓN LIMPIAR
        # ==================================

        tk.Button(
            ventana,
            text="Limpiar",
            width=25,
            command=self.limpiar
        ).pack(pady=5)

        # ==================================
        # BOTÓN SALIR
        # ==================================

        tk.Button(
            ventana,
            text="Salir",
            width=25,
            command=ventana.destroy
        ).pack(pady=5)

    # ======================================
    # REGISTRAR EMPLEADO
    # ======================================

    def registrar_empleado(self):

        nombre = self.entrada_nombre.get().strip()

        # Validar que se haya ingresado un nombre
        if not nombre:
            messagebox.showerror(
                "Error",
                "Debe ingresar el nombre del empleado."
            )

            return

        # Obtener la edad
        texto_edad = self.entrada_edad.get().strip()

        # Verificar que sea un número entero
        try:
            edad = int(texto_edad)

        except ValueError:
            messagebox.showerror(
                "Error",
                "La edad debe ser un número entero."
            )

            return

        # ==================================
        # ASIGNAR DATOS MEDIANTE PROPIEDADES
        # ==================================

        self.empleado.nombre = nombre

        try:
            # La propiedad edad se encarga de validar
            # el valor recibido.
            self.empleado.edad = edad

        except ValueError as error:
            messagebox.showerror(
                "Edad no válida",
                str(error)
            )

            return

        # ==================================
        # MOSTRAR RESULTADO
        # ==================================

        self.resultado.config(
            text=(
                "Empleado registrado correctamente.\n\n"
                f"Nombre: {self.empleado.nombre}\n"
                f"Edad: {self.empleado.edad}"
            )
        )

        messagebox.showinfo(
            "Registro exitoso",
            "El empleado ha sido registrado correctamente."
        )

    # ======================================
    # LIMPIAR CAMPOS
    # ======================================

    def limpiar(self):

        self.entrada_nombre.delete(0, tk.END)
        self.entrada_edad.delete(0, tk.END)

        self.resultado.config(
            text="Ingrese los datos del empleado."
        )


# ==========================================
# INICIAR APLICACIÓN
# ==========================================

ventana = tk.Tk()

app = Aplicacion(ventana)

ventana.mainloop()