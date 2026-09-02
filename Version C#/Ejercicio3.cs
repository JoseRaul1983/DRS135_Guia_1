using System;

// Clase base
public class Vehiculo
{
    // Método para arrancar el vehículo
    public void Arrancar()
    {
        Console.WriteLine("\nEl vehículo ha arrancado.");
        Console.WriteLine("<Metodo original de la clase Vehiculo>");
    }

    // Método para detener el vehículo
    public void Detener()
    {
        Console.WriteLine("\nEl vehículo se ha detenido.");
        Console.WriteLine("<Metodo original de la clase Vehiculo>");
    }
}

// Clase derivada que hereda de Vehiculo
public class Coche : Vehiculo
{
    // Método propio de la clase Coche
    public void Conducir()
    {
        Console.WriteLine("\nEl coche está siendo conducido.");
        Console.WriteLine("<Metodo de la clase derivada Coche>.");
    }
}

// Clase principal
public class Ejercicio3
{
    public static void Main(string[] args)
    {
        Console.Clear();

        Console.WriteLine("========================================");
        Console.WriteLine("     EJERCICIO 3: HERENCIA SIMPLE");
        Console.WriteLine("========================================");

        // Crear una instancia de la clase Coche
        Coche miCoche = new Coche();

        int opcion;

        do
        {
            Console.WriteLine("\n¿Qué desea hacer con el coche?");
            Console.WriteLine("1. Arrancar");
            Console.WriteLine("2. Conducir");
            Console.WriteLine("3. Detener");
            Console.WriteLine("4. Salir");
            Console.Write("Seleccione una opción: ");

            // Validar que el usuario ingrese un número
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
                    // Método heredado de Vehiculo
                    miCoche.Arrancar();
                    break;

                case 2:
                    // Método propio de Coche
                    miCoche.Conducir();
                    break;

                case 3:
                    // Método heredado de Vehiculo
                    miCoche.Detener();
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