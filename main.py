#1.Filtrar elementos: Utiliza listas y comprensiones para filtrar elementos basados en ciertos criterios. Por ejemplo, puedes filtrar una lista de números para obtener solo los números pares o impares, o filtrar una lista de cadenas para obtener solo las que contengan ciertas letras.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares
numeros_pares = [numero for numero in numeros if numero % 2 == 0]

# Filtrar números impares
numeros_impares = [numero for numero in numeros if numero % 2 != 0]

print("Números pares:", numeros_pares)
print("Números impares:", numeros_impares)

print("************************************")

#2. Operaciones matemáticas: Utiliza listas o tuplas para realizar operaciones matemáticas en conjuntos de datos. Por ejemplo, puedes sumar los elementos de una lista, obtener el producto de una tupla o calcular la media de una lista de números.

# Lista de números

# Sumar los elementos de la lista
suma_numeros = sum(numeros)

print("Suma de los elementos de la lista:", suma_numeros)

print("************************************")

#3. Acceder y modificar elementos: Utiliza índices para acceder a elementos específicos en listas, tuplas o diccionarios. También puedes modificar los valores de los elementos si es necesario.

#Acceder

primer_elemento = numeros[0]
print("Primer elemento:", primer_elemento)

quinto_elemento = numeros[4]
print("Quinto elemento:", quinto_elemento)

ultimo_elemento = numeros[-1]
print("Último elemento:", ultimo_elemento)


print("************************************")

#Modificar

numeros[0] = 100
print("Lista después de modificar el primer elemento:", numeros)


numeros[4] = 500
print("Lista después de modificar el quinto elemento:", numeros)

numeros[-1] = 1000
print("Lista después de modificar el último elemento:", numeros)