using System;

class Animal
{
    public virtual void HacerSonido()
    {
        Console.WriteLine("El animal hace un sonido.");
    }
}

class Perro : Animal
{
    public override void HacerSonido()
    {
        Console.WriteLine("El perro hace el sonido: ¡Guau!");
    }
}

class Gato : Animal
{
    public override void
    HacerSonido()
    {
        Console.WriteLine("El gato hace el sonido: ¡Miau!");
    }
}

class SonidoAnimal
{
    static void Main()
    { 
        Console.Clear();

        Console.WriteLine("========================================");
        Console.WriteLine("       EJERCICIO 4: POLIMORFISMO");
        Console.WriteLine("========================================");

        Animal animal;
        string opcion = "";
        while (opcion != "3")
        { 
            Console.WriteLine("\n----------------------------------------");
            Console.WriteLine("           MENÚ DEL EJERCICIO");
            Console.WriteLine("----------------------------------------");
            Console.WriteLine("1. Perro");
            Console.WriteLine("2. Gato");
            Console.WriteLine("3. Salir");
            Console.Write("Seleccione una opción: ");
            
            opcion = Console.ReadLine();
            
            if (opcion == "1")
            {
                animal = new Perro();
                animal.HacerSonido();
            } 
            else if (opcion == "2")
            { 
                animal = new Gato();
                animal.HacerSonido();
            } 
            else if (opcion == "3")
            {
                Console.WriteLine("Programa finalizado.");
            }
            else { Console.WriteLine("Opción no válida. Intente nuevamente.");
            }
        }
    }
}