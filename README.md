# DRS135_Guia_1

Se ha desarrollado dos versiones para cada ejercicio, tanto en C# como en Python (entorno gráfico), las cuales pueden notarse en las carpetas denominadas
"Version C#" y "Version Python".

Contiene el desarrollo de Guia Practica # 1

Ejercicios a desarrollar:
• Ejercicio 1: Implementación de Abstracción de Datos
Objetivo: Implementar un tipo de datos abstracto que oculta detalles de implementación.
Enunciado:
Crea una clase CuentaBancaria que represente una cuenta bancaria. Utiliza abstracción de datos para ocultar el detalle de la implementación del saldo y solo permite el acceso a través de los métodos públicos. Los métodos deben permitir realizar operaciones como depositar, retirar y consultar el saldo.
Instrucciones:
• Define la clase CuentaBancaria con un atributo privado para el saldo.
• Implementa los métodos:
• Depositar(decimal monto): permite agregar dinero a la cuenta.
• Retirar(decimal monto): permite retirar dinero de la cuenta.
• ObtenerSaldo(): devuelve el saldo actual.
• Los métodos deben validar que los montos sean positivos y que no haya fondos insuficientes para la operación de retiro.

• Ejercicio 2: Encapsulación y Control de Acceso
Objetivo: Aplicar la encapsulación para proteger los datos y controlar el acceso a los métodos de una clase.
Enunciado:
Crea una clase Empleado que tenga dos atributos privados: nombre y edad. Implementa encapsulación para acceder a estos atributos a través de propiedades. Asegúrate de que la edad solo pueda ser modificada a través de un valor válido (mayor que 0 y menor que 100).
Instrucciones:
• Define la clase Empleado con los atributos privados.
• Usa propiedades para controlar el acceso a nombre y edad.
• La propiedad de edad debe validar que el valor sea positivo y menor que 100.

• Ejercicio 3: Herencia Simple
Objetivo: Implementar herencia simple para extender las funcionalidades de una clase base.
Enunciado:
Crea una clase base Vehiculo que tenga los métodos Arrancar() y Detener(). Luego, crea una clase derivada Coche que herede de Vehiculo y añada un método Conducir(). Asegúrate de que el Coche pueda usar los métodos heredados de Vehiculo y su propio método Conducir().
Instrucciones:
• Define la clase base Vehiculo con los métodos Arrancar() y Detener().
• Define la clase derivada Coche que herede de Vehiculo y añada el método Conducir().
• Crea una instancia de Coche y usa todos los métodos.

• Ejercicio 4: Polimorfismo
Objetivo: Implementar polimorfismo utilizando métodos sobrescritos.
Enunciado:
Crea una clase base Animal con un método HacerSonido(). Luego, crea dos clases derivadas: Perro y Gato, que sobrescriban el método HacerSonido() para hacer un sonido diferente. Utiliza una referencia de tipo Animal para llamar al método HacerSonido() y demostrar el polimorfismo.
Instrucciones:
• Define la clase base Animal con el método HacerSonido().
• Sobrescribe HacerSonido() en las clases Perro y Gato.
• Crea instancias de Perro y Gato, y usa una referencia de tipo Animal para llamar al método.

Ejercicio 5: Herencia Multinivel y Sobrescritura de Métodos
Objetivo: Demostrar herencia multinivel y sobrescritura de métodos.
Enunciado:
Crea una jerarquía de clases en la que Animal sea la clase base, Mamifero sea una clase intermedia y Perro sea una clase derivada. Asegúrate de que Perro herede los métodos de Mamifero y Animal, y sobrescriba el método HacerSonido().
Instrucciones:
• Define la clase base Animal con un método HacerSonido().
• Define la clase intermedia Mamifero que herede de Animal y añada un método Alimentar().
• Define la clase Perro que herede de Mamifero y sobrescriba HacerSonido().
• Crea instancias y demuestra la llamada a los métodos heredados y sobrescritos.
