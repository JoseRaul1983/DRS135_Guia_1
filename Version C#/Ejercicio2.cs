using System;

// Clase con encapsulación para proteger los datos
public class Empleado
{
    // Campos privados: no pueden ser modificados directamente
    // desde fuera de la clase.
    private string _nombre;
    private int _edad;

    // Propiedad Nombre
    public string Nombre
    {
        get { return _nombre; }
        set { _nombre = value; }
    }

    // Propiedad Edad con validación
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
                Console.WriteLine(
                    $"[Error] La edad ingresada ({value}) no es válida. " +
                    "Debe estar entre 1 y 99."
                );
            }
        }
    }
}

public class Ejercicio2
{
    public static void Main(string[] args)
    {
        Console.Clear();

        Console.WriteLine("========================================");
        Console.WriteLine(" EJERCICIO 2: ENCAPSULACIÓN Y CONTROL");
        Console.WriteLine("             DE ACCESO");
        Console.WriteLine("========================================");

        // Crear un objeto de tipo Empleado
        Empleado emp = new Empleado();

        // Asignar datos válidos
        Console.WriteLine("\nAsignando datos válidos...");

        emp.Nombre = "Juan Pérez";
        emp.Edad = 28;

        Console.WriteLine(
            $"Empleado registrado: Nombre = {emp.Nombre}, Edad = {emp.Edad}"
        );

        // Intentar asignar una edad inválida
        Console.WriteLine("\nIntentando asignar una edad de 105...");
        emp.Edad = 105;

        // Intentar asignar una edad negativa
        Console.WriteLine("\nIntentando asignar una edad de -5...");
        emp.Edad = -5;

        // Mostrar los datos finales
        Console.WriteLine(
            $"\nDatos finales del empleado: " +
            $"Nombre = {emp.Nombre}, Edad = {emp.Edad}"
        );

        Console.WriteLine("\n========================================");
        Console.WriteLine("Presione ENTER para finalizar...");
        Console.ReadLine();
    }
}