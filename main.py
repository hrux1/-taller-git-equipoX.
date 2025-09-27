# Equipo X - Proyecto de operaciones matemáticas básicas
# Este proyecto contiene funciones para realizar operaciones simples

import math

def raiz(c):
    resultado = math.sqrt(c)
    if resultado.is_integer():
        return int(resultado)
    return resultado

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def potencia(a, b):
    return a ** b

if __name__ == "__main__":
    print("Suma 5 + 3:", suma(5, 3))
    print("Resta 10 - 4:", resta(10, 4))
    print("Multiplicación 2 x 6:", multiplicacion(2, 6))
    print("Raíz cuadrada de 9:", raiz(9))
    print("Potencia 2 ^ 3:", potencia(2, 3))