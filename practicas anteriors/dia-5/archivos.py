#creamos un diccionario para guardar el csv convertido
usuarios = {} 
nomFitxer = "nom-email.csv"

def loadUsuarios(nombreArchivo, user_dict):
    #abrimos el archivo, 
    with open(nombreArchivo) as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                partes = linea.split(",")
                if len(partes) == 2:
                    user_dict[partes[0].lower()] = partes[1]


def buscarEmail(busquedaNombre):
    busquedaNombre = busquedaNombre.lower()
    if busquedaNombre in usuarios:
        return usuarios[busquedaNombre]
    else:
        return None


loadUsuarios(nomFitxer, usuarios)



