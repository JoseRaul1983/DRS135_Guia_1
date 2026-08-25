using System;

class CuentaBancaria
{
    private decimal saldo;

    public CuentaBancaria(decimal saldoInicial)
    {
        if (saldoInicial < 0)
        {
            throw new ArgumentException("El saldo inicial no puede ser negativo.");
        }

        saldo = saldoInicial;
    }

    public void Depositar(decimal monto)
    {
        if (monto <= 0)
        {
            throw new ArgumentException("El monto a depositar debe ser positivo.");
        }

        saldo += monto;
    }

    public void Retirar(decimal monto)
    {
        if (monto <= 0)
        {
            throw new ArgumentException("El monto a retirar debe ser positivo.");
        }

        if (monto > saldo)
        {
            throw new InvalidOperationException("Fondos insuficientes.");
        }

        saldo -= monto;
    }

    public decimal ObtenerSaldo()
    {
        return saldo;
    }
}

class Program
{
    static void Main()
    {
        CuentaBancaria cuenta = new CuentaBancaria(1000);

        cuenta.Depositar(500);
        cuenta.Retirar(200);

        Console.WriteLine("Saldo actual: " + cuenta.ObtenerSaldo());
    }
}