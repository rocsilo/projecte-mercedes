from datetime import datetime

nombre = input("Tu nombre: ")
edad = int(input("Tu edad: "))

año_100 = datetime.now().year + (100 - edad)

if edad >= 100:
    print('tonto')
else:
    print(f"{nombre}, cumplirás 100 años en {año_100}")

