using System;

class Animal
{
    public virtual void HacerSonido()
    {
        Console.WriteLine("El animal hace un sonido.");
    }
}

class Mamifero : Animal
{
    public void Alimentar()
    {
        Console.WriteLine("El mamífero se está alimentando.");
    }
}

class Perro : Mamifero
{
    public override void HacerSonido()
    {
        Console.WriteLine("El perro hace el sonido: ¡Guau!");
    }
}

class Program
{
    static void Main()
    {
        Perro perro = new Perro();

        Console.WriteLine("Validando la herencia multinivel y sobreescritura de metodo");

        perro.HacerSonido();
        perro.Alimentar();
    }
}