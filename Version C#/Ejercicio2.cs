using System;

// Clase con encapsulación para proteger los datos
public class Empleado
{
    // Atributos privados: no pueden ser modificados directamente
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
            // La edad debe ser mayor que 0 y menor que 100
            if (value > 0 && value < 100)
            {
                _edad = value;
            }
            else
            {
                throw new ArgumentException(
                    "La edad debe ser mayor que 0 y menor que 100."
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

        // Solicitar el nombre al usuario
        Console.Write("\nIngrese el nombre del empleado: ");
        emp.Nombre = Console.ReadLine();

        // Solicitar la edad al usuario
        while (true)
        {
            Console.Write("Ingrese la edad del empleado: ");

            // Primero comprobamos que el usuario haya ingresado
            // un número entero válido.
            if (!int.TryParse(Console.ReadLine(), out int edad))
            {
                Console.WriteLine(
                    "[Error] Debe ingresar un número entero."
                );

                continue;
            }

            try
            {
                // La propiedad Edad recibe el valor y se encarga
                // de determinar si es válido.
                emp.Edad = edad;

                // Si no se produjo ningún error, la edad es válida.
                break;
            }
            catch (ArgumentException ex)
            {
                // Mostrar el mensaje generado por la propiedad
                // cuando la edad no cumple las condiciones.
                Console.WriteLine($"[Error] {ex.Message}");
            }
        }

        // Mostrar los datos del empleado
        Console.WriteLine("\n========================================");
        Console.WriteLine("       EMPLEADO REGISTRADO");
        Console.WriteLine("========================================");

        Console.WriteLine($"Nombre: {emp.Nombre}");
        Console.WriteLine($"Edad:   {emp.Edad}");

        Console.WriteLine("\nPresione ENTER para finalizar...");
        Console.ReadLine();
    }
}