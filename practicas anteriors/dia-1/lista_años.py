# Lista con años de nacimiento
años_nacimiento = [1990, 1995, 2000, 2005, 2010]

# Obtener el año actual
from datetime import datetime
año_actual = datetime.now().year

# Generar lista de edades
edades = []

for año in años_nacimiento:
    edad = año_actual - año
    edades.append(edad)

print("Años de nacimiento:", años_nacimiento)
print("Edades:", edades)