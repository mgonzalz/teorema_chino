from teorema_chino import teorema_chino_resto
# Ejercicio del proyecto
coefficients = [8, 3, 5]
modulos = [13, 11, 8]
x = teorema_chino_resto(coefficients, modulos)
for i in range(len(coefficients)):
    print(coefficients[i], "mod", modulos[i], "=", coefficients[i] % modulos[i])
print("La solución es:", x)
