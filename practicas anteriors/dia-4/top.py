import csv

# 1. Llegim els noms de les estacions i els guardem
noms_estacions = {}

with open('estacions.csv', mode='r') as fitxer:
    lector = csv.DictReader(fitxer)
    for fila in lector:
        codigo = fila['CODI_ESTACIO']
        nombre = fila['NOM_ESTACIO']
        noms_estacions[codigo] = nombre

# 2. Busquem la temperatura mínima
temp_minima = 100.0
guanyador = {}

with open('mesures.csv', mode='r') as fitxer:
    lector = csv.DictReader(fitxer)
    for fila in lector:
        # Al teu fitxer, la columna es diu 'ACRÒNIM' amb accent
        if fila['ACRÒNIM'] == 'TN':
            valor = float(fila['VALOR'])
            
            if valor < temp_minima:
                temp_minima = valor
                guanyador = fila

# 3. Mostrem el resultat
print("Temperatura mínima:", temp_minima)
print("Data:", guanyador['DATA_LECTURA'])

codi_trobat = guanyador['CODI_ESTACIO']
nom_trobat = noms_estacions[codi_trobat]
print("Estació:", nom_trobat)