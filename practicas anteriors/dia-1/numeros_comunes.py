# Dos listas de números con distinta longitud
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9, 10]

# Encontrar números que están en ambas listas
numeros_comunes = []

for numero in lista1:
    if numero in lista2:
        numeros_comunes.append(numero)

print("Números en común:", numeros_comunes)