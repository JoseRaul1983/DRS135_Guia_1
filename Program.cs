using System;

namespace actividad1_poo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            bool salir = false;

            while (!salir)
            {
                Console.Clear();
                Console.WriteLine("========================================");
                Console.WriteLine("      ACTIVIDAD 1 - GUÍA EVALUADA POO   ");
                Console.WriteLine("========================================");
                Console.WriteLine("1. Ejercicio 2: Encapsulación");
                Console.WriteLine("2. Ejercicio 3: Herencia Simple");
                Console.WriteLine("3. Salir");
                Console.WriteLine("========================================");
                Console.Write("Seleccione una opción: ");

                string? opcion = Console.ReadLine();

                switch (opcion)
                {
                    case "1":
                        Ejercicio2.Ejecutar();
                        break;
                    case "2":
                        Ejercicio3.Ejecutar();
                        break;
                    case "3":
                        salir = true;
                        Console.WriteLine("\nSaliendo del programa...");
                        continue;
                    default:
                        Console.WriteLine("\nOpción no válida.");
                        break;
                }

                Console.WriteLine("\nPresione cualquier tecla para volver al menú...");
                Console.ReadKey();
            }
        }
    }
}