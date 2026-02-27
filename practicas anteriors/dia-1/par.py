numero = int(input("Tu numero: "))
otronumero = int(input("Tu 2ndo numero: "))

if numero % otronumero == 0:
    print("El numero", numero, "es divisible por", otronumero)
elif numero % 4 == 0:
    print("Es múltiplo de 4")
elif numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")