from teorema_chino import teorema_chino_resto, sistema
# Ejercicio del proyecto
sol = [8, 3, 5]
modulos = [13, 11, 8]
sistema(sol, modulos)
x = teorema_chino_resto(sol, modulos)
print('La solución es:', x)


# Ejercicio de ejemplo
sol = [2,4,5]
modulos = [5,7,11]
sistema(sol, modulos)
x = teorema_chino_resto(sol, modulos)
print('La solución es:', x)

# Ejercicio de ejemplo
sol = [1,10]
modulos = [7, 11]
sistema(sol, modulos)
x = teorema_chino_resto(sol, modulos)
print('La solución es:', x)
