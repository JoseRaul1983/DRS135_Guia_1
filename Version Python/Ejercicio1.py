class CuentaBancaria:
    def __init__(self, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")

        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")

        self.__saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")

        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes.")

        self.__saldo -= monto

    def obtener_saldo(self):
        return self.__saldo


cuenta = CuentaBancaria(1000)

cuenta.depositar(500)
cuenta.retirar(200)

print("Saldo actual:", cuenta.obtener_saldo())