using System;

// Clase base
class Animal
{
    // Método virtual que puede ser sobrescrito por las clases derivadas
    public virtual void HacerSonido()
    {
        Console.WriteLine("El animal hace un sonido.");
    }
}

// Clase intermedia que hereda de Animal
class Mamifero : Animal
{
    // Método propio de Mamifero
    public void Alimentar()
    {
        Console.WriteLine("El mamífero se está alimentando.");
    }
}

// Clase derivada que hereda de Mamifero
class Perro : Mamifero
{
    // Sobrescritura del método HacerSonido() de Animal
    public override void HacerSonido()
    {
        Console.WriteLine("El perro hace el sonido ¡Guau!");
    }
}

class Program
{
    static void Main()
    {
        Console.Clear();

        Console.WriteLine("========================================");
        Console.WriteLine(" EJERCICIO 5: HERENCIA MULTINIVEL Y");
        Console.WriteLine("          SOBREESCRITURA");
        Console.WriteLine("========================================");

        // Se crea una instancia de Perro.
        // Perro hereda de Mamifero y Mamifero hereda de Animal.
        Perro perro = new Perro();

        int opcion;

        do
        {
            Console.WriteLine("\n----------------------------------------");
            Console.WriteLine("           MENÚ DEL EJERCICIO");
            Console.WriteLine("----------------------------------------");
            Console.WriteLine("1. Hacer sonido");
            Console.WriteLine("2. Alimentar");
            Console.WriteLine("3. Demostrar toda la herencia");
            Console.WriteLine("4. Salir");
            Console.Write("Seleccione una opción: ");

            // Valida que el usuario ingrese un número
            if (!int.TryParse(Console.ReadLine(), out opcion))
            {
                Console.WriteLine(
                    "\n[Error] Debe ingresar un número del 1 al 4."
                );

                continue;
            }

            switch (opcion)
            {
                case 1:
                    Console.WriteLine("\n[Método sobrescrito]");

                    // Se ejecuta la versión sobreescrita por Perro
                    perro.HacerSonido();

                    break;

                case 2:
                    Console.WriteLine("\n[Método heredado de Mamifero]");

                    // Perro hereda este método de la clase Mamifero
                    perro.Alimentar();

                    break;

                case 3:
                    Console.WriteLine(
                        "\n[Demostración de la herencia multinivel]"
                    );

                    Console.WriteLine(
                        "\n1. Animal -> define HacerSonido()"
                    );

                    Console.WriteLine(
                        "2. Mamifero -> hereda de Animal y añade Alimentar()"
                    );

                    Console.WriteLine(
                        "3. Perro -> hereda de Mamifero y sobreescribe HacerSonido()"
                    );

                    Console.WriteLine("\nEjecutando HacerSonido():");
                    perro.HacerSonido();

                    Console.WriteLine("\nEjecutando Alimentar():");
                    perro.Alimentar();

                    break;

                case 4:
                    Console.WriteLine(
                        "\nEl programa ha finalizado."
                    );

                    break;

                default:
                    Console.WriteLine(
                        "\n[Error] Opción no válida. " +
                        "Seleccione una opción del 1 al 4."
                    );

                    break;
            }

        } while (opcion != 4);

        Console.WriteLine("\nPresione ENTER para cerrar...");
        Console.ReadLine();
    }
}