using System;

public class Vehiculo
{
    public void Arrancar()
    {
        Console.WriteLine("El vehículo ha arrancado y el motor está en marcha.");
    }

    public void Detener()
    {
        Console.WriteLine("El vehículo se ha detenido por completo.");
    }
}

public class Coche : Vehiculo
{
    public void Conducir()
    {
        Console.WriteLine("El coche está siendo conducido por la carretera.");
    }
}

public class Ejercicio3
{
    public static void Main(string[] args)
    {
        Console.Clear();

        Console.WriteLine("========================================");
        Console.WriteLine("     EJERCICIO 3: HERENCIA SIMPLE");
        Console.WriteLine("========================================");

        Coche miCoche = new Coche();

        Console.WriteLine("\n--- Llamando a Arrancar() [Heredado] ---");
        miCoche.Arrancar();

        Console.WriteLine("\n--- Llamando a Conducir() [Propio] ---");
        miCoche.Conducir();

        Console.WriteLine("\n--- Llamando a Detener() [Heredado] ---");
        miCoche.Detener();

        Console.WriteLine("\n========================================");
        Console.WriteLine("Presione ENTER para finalizar...");
        Console.ReadLine();
    }
}