palabra = input("Ingresa una palabra: ").lower()

es_palindromo = True
for primera in range(len(palabra)):
    if palabra[primera] != palabra[len(palabra) - 1 - primera]:
        es_palindromo = False
        break

if es_palindromo:
    print("SÍ es palíndromo")
else:
    print("NO es palíndromo")