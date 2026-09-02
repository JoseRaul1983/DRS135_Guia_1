import tkinter as tk
from tkinter import messagebox

# Clase base
class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido.")

# Clase Perro
class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace el sonido ¡Guau!")
        return "El perro hace el sonido ¡Guau!"

# Clase gato
class Gato(Animal):
    def hacer_sonido(self):
        print("El gato hace el sonido ¡Miau!")
        return "El gato hace el sonido ¡Miau!"

# Interfaz gráfica
class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana

        # Configuración de la ventana
        self.ventana.title(
            "Ejercicio 4 - Polimorfismo"
        )

        self.ventana.geometry("550x550")
        self.ventana.resizable(False, False)

        # Variable para almacenar el animal seleccionado
        self.animal = None

        # Título
        titulo = tk.Label(
            ventana,
            text="EJERCICIO 4: POLIMORFISMO",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=20)

        subtitulo = tk.Label(
            ventana,
            text="Seleccione un animal y haga que produzca un sonido.",
            font=("Arial", 11)
        )

        subtitulo.pack()

        tk.Label(
            ventana,
            text="-" * 55
        ).pack(pady=10)

        # Selección de animal
        
        tk.Label(
            ventana,
            text="Seleccione un animal:",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        self.opcion_animal = tk.StringVar(value="ninguno")
        
        # Botón de opción Perro
        tk.Radiobutton(
            ventana,
            text="Perro",
            variable=self.opcion_animal,
            value="Perro",
            font=("Arial", 11)
        ).pack(pady=5)

        # Botón de opción Gato
        tk.Radiobutton(
            ventana,
            text="Gato",
            variable=self.opcion_animal,
            value="Gato",
            font=("Arial", 11)
        ).pack(pady=5)

        # Botón hacer sonido
        tk.Button(
            ventana,
            text="Hacer sonido",
            width=25,
            command=self.hacer_sonido
        ).pack(pady=20)

        # Resultado
        self.resultado = tk.Label(
            ventana,
            text="Seleccione un animal.",
            font=("Arial", 13, "bold"),
            justify="center",
            wraplength=450
        )

        self.resultado.pack(pady=20)

        # Mensaje
        self.explicacion = tk.Label(
            ventana,
            text=(
                "El método hacer_sonido() se ejecuta de manera "
                "diferente según el objeto seleccionado."
            ),
            font=("Arial", 10),
            justify="center",
            wraplength=450
        )

        self.explicacion.pack(pady=10)

        # Botón Limpiar
        tk.Button(
            ventana,
            text="Limpiar",
            width=25,
            command=self.limpiar
        ).pack(pady=5)

        # Botón salir
        tk.Button(
            ventana,
            text="Salir",
            width=25,
            command=ventana.destroy
        ).pack(pady=5)

    # Ejecutar polimorfismo
    def hacer_sonido(self):

        seleccion = self.opcion_animal.get()

        if seleccion == "":
            messagebox.showwarning(
                "Selección requerida",
                "Debe seleccionar un animal."
            )

            return

        # Se crea el objeto
        if seleccion == "Perro":
            self.animal = Perro()

        elif seleccion == "Gato":
            self.animal = Gato()

        # Referencia de tipo animal
        animal: Animal = self.animal

        # Misma llamada produce un resultado diferente dependiendo del objeto.
        resultado = animal.hacer_sonido()

        self.resultado.config(
            text=resultado
        )

        # Mostrar una explicación adicional
        if seleccion == "Perro":
            self.explicacion.config(
                text=(
                    "Se utilizó una referencia de tipo Animal "
                    "que apunta a un objeto Perro. "
                    "\nSe ejecutó el método hacer_sonido() de Perro."
                )
            )

        else:
            self.explicacion.config(
                text=(
                    "Se utilizó una referencia de tipo Animal "
                    "que apunta a un objeto Gato. "
                    "\nSe ejecutó el método hacer_sonido() de Gato."
                )
            )

    # Limpiar la interfaz
    def limpiar(self):

        self.opcion_animal.set("ninguno")

        self.animal = None

        self.resultado.config(
            text="Seleccione un animal."
        )

        self.explicacion.config(
            text=(
                "El método hacer_sonido() se ejecuta de manera "
                "diferente según el objeto seleccionado."
            )
        )

# Iniciar aplicación

ventana = tk.Tk()

app = Aplicacion(ventana)

ventana.mainloop()