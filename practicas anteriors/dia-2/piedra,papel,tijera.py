seguir_jugando = True

# Diccionario con todas las palabras válidas
palabras_validas = {
    "piedra": ["piedra", "piedrote", "roca", "piedrón", "rock", "stone" , "malphite"],
    "papel": ["papel", "papelito", "hoja", "paper", "cartón" "talon"],
    "tijera": ["tijera", "tijeras", "tijerita", "cortadora", "scissors" "gwen"]
}

while seguir_jugando:
    # Jugador 1 elige
    jugador1 = input("Jugador 1 - Elige: piedra, papel o tijera: ").lower()
    
    # Jugador 2 elige  
    jugador2 = input("Jugador 2 - Elige: piedra, papel o tijera: ").lower()
    
    # Mostrar elecciones
    print(f"Jugador 1 eligió: {jugador1}")
    print(f"Jugador 2 eligió: {jugador2}")
    
    # Determinar ganador
    if jugador1 == jugador2:
        print("¡Empate!")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        print("¡Jugador 1 gana!")
    else:
        print("¡Jugador 2 gana!")
    
    # Preguntar si quieren seguir jugando
    respuesta = input("¿Quieren seguir jugando? (si/no): ").lower()
    if  respuesta != "si":
        seguir_jugando = False
        print("¡Gracias por jugar!")