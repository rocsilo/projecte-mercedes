import random

numero = random.randint(1, 9)
intentos = 0
continuar = True


while continuar:
    entrada = input("Adivina un número del 1 al 9 (o escribe 'exit' para salir): ")
    intentos += 1
    if entrada == "exit":
        print("¡Hasta luego!")
        continuar = False
    elif entrada.isdigit() and int(entrada) == numero:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
        continuar = False
    else:
        print("Incorrecto, sigue intentando.")