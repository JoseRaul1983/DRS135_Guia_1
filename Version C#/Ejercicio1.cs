using System;

class CuentaBancaria
{
    // Encapsulamiento:
    // El saldo solamente puede modificarse mediante
    // los métodos de esta clase.
    private decimal saldo;

    // El saldo inicia en $0.00
    public CuentaBancaria()
    {
        saldo = 0;
    }

    // Método para depositar dinero
    public void Depositar(decimal monto)
    {
        if (monto <= 0)
        {
            throw new ArgumentException(
                "El monto a depositar debe ser mayor que $0.00."
            );
        }

        saldo += monto;
    }

    // Método para retirar dinero
    public void Retirar(decimal monto)
    {
        if (monto <= 0)
        {
            throw new ArgumentException(
                "El monto a retirar debe ser mayor que $0.00."
            );
        }

        if (monto > saldo)
        {
            throw new InvalidOperationException(
                $"Fondos insuficientes. Su saldo disponible es ${saldo:F2}."
            );
        }

        saldo -= monto;
    }

    // Método para consultar el saldo
    public decimal ObtenerSaldo()
    {
        return saldo;
    }
}

class Program
{
    static void Main()
    {
        CuentaBancaria cuenta = new CuentaBancaria();

        bool continuar = true;

        while (continuar)
        {
            Console.Clear();

            Console.WriteLine("========================================");
            Console.WriteLine("          CUENTA BANCARIA");
            Console.WriteLine("========================================");
            Console.WriteLine($"Saldo actual: ${cuenta.ObtenerSaldo():F2}");
            Console.WriteLine("========================================");
            Console.WriteLine("1. Depositar dinero");
            Console.WriteLine("2. Retirar dinero");
            Console.WriteLine("3. Consultar saldo");
            Console.WriteLine("4. Salir");
            Console.WriteLine("========================================");
            Console.Write("Seleccione una opción: ");

            string? opcion = Console.ReadLine();

            switch (opcion)
            {
                case "1":
                    Depositar(cuenta);
                    break;

                case "2":
                    Retirar(cuenta);
                    break;

                case "3":
                    Console.WriteLine();
                    Console.WriteLine(
                        $"Su saldo actual es: ${cuenta.ObtenerSaldo():F2}"
                    );

                    Pausar();
                    break;

                case "4":
                    continuar = false;
                    Console.WriteLine();
                    Console.WriteLine(
                        "Gracias por utilizar el programa."
                    );
                    break;

                default:
                    Console.WriteLine();
                    Console.WriteLine(
                        "[ERROR] La opción seleccionada no es válida."
                    );

                    Pausar();
                    break;
            }
        }
    }

    // Solicita y valida el monto del depósito
    static void Depositar(CuentaBancaria cuenta)
    {
        Console.WriteLine();
        Console.Write("Ingrese el monto a depositar: ");

        string? entrada = Console.ReadLine();

        // Validar que sea un número válido
        if (!decimal.TryParse(entrada, out decimal monto))
        {
            Console.WriteLine();
            Console.WriteLine(
                "[ERROR] Debe ingresar un valor numérico válido."
            );

            Pausar();
            return;
        }

        try
        {
            cuenta.Depositar(monto);

            Console.WriteLine();
            Console.WriteLine(
                $"Depósito realizado correctamente: ${monto:F2}"
            );

            Console.WriteLine(
                $"Nuevo saldo: ${cuenta.ObtenerSaldo():F2}"
            );
        }
        catch (ArgumentException ex)
        {
            Console.WriteLine();
            Console.WriteLine($"[ERROR] {ex.Message}");
        }

        Pausar();
    }

    // Solicita y valida el monto del retiro
    static void Retirar(CuentaBancaria cuenta)
    {
        Console.WriteLine();
        Console.Write("Ingrese el monto a retirar: ");

        string? entrada = Console.ReadLine();

        // Validar que sea un número válido
        if (!decimal.TryParse(entrada, out decimal monto))
        {
            Console.WriteLine();
            Console.WriteLine(
                "[ERROR] Debe ingresar un valor numérico válido."
            );

            Pausar();
            return;
        }

        try
        {
            cuenta.Retirar(monto);

            Console.WriteLine();
            Console.WriteLine(
                $"Retiro realizado correctamente: ${monto:F2}"
            );

            Console.WriteLine(
                $"Nuevo saldo: ${cuenta.ObtenerSaldo():F2}"
            );
        }
        catch (ArgumentException ex)
        {
            Console.WriteLine();
            Console.WriteLine($"[ERROR] {ex.Message}");
        }
        catch (InvalidOperationException ex)
        {
            Console.WriteLine();
            Console.WriteLine($"[ERROR] {ex.Message}");
        }

        Pausar();
    }

    // Pausa el programa para que el usuario pueda leer el resultado
    static void Pausar()
    {
        Console.WriteLine();
        Console.WriteLine("Presione ENTER para continuar...");
        Console.ReadLine();
    }
}