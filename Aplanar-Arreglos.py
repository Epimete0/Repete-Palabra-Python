# Ejercicio que muestra como aplanar un arreglo de 2 dimensiones
# a un arreglo de 1 dimension
#

# Arreglo de prueba

arreglo = [[1, 2, 3], [4, 5, 6],[[1,24,5]], [7, 8, 9]]
            # Resultado esperado : [1, 2, 3, 4, 5, 6, [1, 24, 5], 7, 8, 9]  
arregloPlano = []

# Proceso

for i in arreglo: # Se itera en el arreglo
    for j in i: # Se itera en el arreglo dentro del arreglo
        arregloPlano.append(j) # Se agrega el valor al arregloPlano

print(arregloPlano)