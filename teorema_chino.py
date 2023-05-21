# PROGRAMA PARA LA RESOLUCION DE UN SISTEMA LINEAL DE CONGRUENCIA 

## Importación de las librerias necesarias

from math import gcd


## Función para el calculo del inverso multiplicativo: Algoritmo de Euclides.

def euclides(a, m):
    if isinstance(a, int) or isinstance(m, int):
        if gcd(a, m) != 1:
            print(' No existe inverso multiplicativo')
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m
        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (
                u1 - q * v1,
                u2 - q * v2,
                u3 - q * v3,
                v1,
                v2,
                v3,
            )
        return u1 % m
    else:
        raise TypeError("Los parámetros deben ser números enteros")

'''
EXPLICACIÓN DEL CÓDIGO:
    - La función recibe dos parámetros: a y m, siendo estos números enteros (Se comprueba).
    - Se comprueba que el máximo común divisor de a y m sea 1, en caso contrario no existe inverso multiplicativo.
A continuación utiliza el algoritmo de euclides para encontrar u1, u2 y u3 que satisfacen la ecuación u1*a +
u2*m = u3. A medida que vaya avanzando el algoritmo, los valores de los coeficientes se van actualizando 
hasta que v3 (el resto) sea igual a 0. Finalmente, devuelve u1 % m como el inverso multiplicativo de a en el 
módulo m.
'''

## Función para el calculo del teorema chino del resto.
def teorema_chino_resto(coefficients, modulos):
    for i in range(len(coefficients)):
        if not isinstance(coefficients[i], int):
            raise TypeError("Los coeficientes deben ser números enteros")
        if not isinstance(modulos[i], int):
            raise TypeError("Los módulos deben ser números enteros")
    if len(coefficients) != len(modulos):
        raise ValueError("El número de coeficientes y módulos no coincide")
    M = 1
    for i in modulos:
        M *= i
    x = 0
    for i in range(len(coefficients)):
        ci = M // modulos[i]
        di = euclides(ci, modulos[i])
        x += coefficients[i] * ci * di
    return x % M

'''
EXPLICACIÓN DEL CÓDIGO:
    - La función recibe dos parámetros: coefficients y modulos, siendo estos listas de números enteros (Se comprueba mediante el for).
    - Se comprueba que el número de coeficientes y módulos sea el mismo.
    - Se calcula el producto de todos los módulos, lo anterior en el trabajo llamado M.
Tras ello, intera sobre los coeficientes y los módulos realizando los calculos necesarios para la obtención de x: Ci*Ni*Di. Para cada coeficiente y módulo, se calcula Ci, siendo el valor de M divido entre cada modulo. Tras ello, se calcula Di, siendo el inverso multiplicativo de Ci en el módulo, ejecutamos para ello la función anterior que permite hallar el inverso. Finalmente, se suma Ci*Ni*Di a la variable x. Finalmente para obtener la solución del sistema de congruencias, se calcula x % M (%: resto de la división).
'''
