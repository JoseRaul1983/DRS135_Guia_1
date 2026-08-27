using System;

namespace actividad1_poo
{
    // Clase con encapsulación para proteger datos
    public class Empleado
    {
        private string _nombre;
        private int _edad;

        public string Nombre
        {
            get { return _nombre; }
            set { _nombre = value; }
        }

        public int Edad
        {
            get { return _edad; }
            set
            {
                if (value > 0 && value < 100)
                {
                    _edad = value;
                }
                else
                {
                    Console.WriteLine($"[Error] La edad ingresada ({value}) no es válida. Debe estar entre 1 y 99.");
                }
            }
        }
    }

    public static class Ejercicio2
    {
        public static void Ejecutar()
        {
            Console.Clear();
            Console.WriteLine("=== EJERCICIO 2: ENCAPSULACIÓN Y CONTROL DE ACCESO ===");

            Empleado emp = new Empleado();

            Console.WriteLine("\nAsignando datos válidos...");
            emp.Nombre = "Juan Pérez";
            emp.Edad = 28;
            Console.WriteLine($"Empleado registrado: Nombre = {emp.Nombre}, Edad = {emp.Edad}");

            Console.WriteLine("\nIntentando asignar una edad de 105...");
            emp.Edad = 105;

            Console.WriteLine("\nIntentando asignar una edad de -5...");
            emp.Edad = -5;

            Console.WriteLine($"\nDatos finales del empleado: Nombre = {emp.Nombre}, Edad = {emp.Edad}");
        }
    }
}