"""
Módulo que proporciona clases para realizar operaciones matemáticas básicas.
Incluye suma, resta y cálculo de promedios.
"""


class OperacionesBasicas:
    """Clase para realizar operaciones básicas de suma y resta."""

    def __init__(self):
        self._resultado = 0

    def sumar(self, a, b):
        """Suma dos números y almacena el resultado."""
        self._resultado = a + b

    def restar(self, a, b):
        """Resta dos números y almacena el resultado."""
        self._resultado = a - b

    @property
    def resultado(self):
        """Devuelve el resultado almacenado."""
        return self._resultado

    @resultado.setter
    def resultado(self, valor):
        """Permite establecer un nuevo valor para el resultado."""
        self._resultado = valor


class CalculadoraPromedio:
    """Clase para calcular el promedio de una lista de valores."""

    def __init__(self, valores):
        self._valores = valores

    def calcular_promedio(self):
        """Calcula y devuelve el promedio de los valores."""
        suma = sum(self._valores)
        return suma / len(self._valores) if self._valores else 0

    @property
    def valores(self):
        """Devuelve la lista de valores almacenada."""
        return self._valores

    @valores.setter
    def valores(self, nuevos_valores):
        """Permite actualizar la lista de valores."""
        self._valores = nuevos_valores


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20


# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.resultado}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.resultado}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {promedio}")
