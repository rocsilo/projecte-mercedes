import archivos
import sys

if len(sys.argv) == 2:
    busquedaNombre = sys.argv[1].lower()
else:
    busquedaNombre = input('Escribe un solo nombre para ver el email:').lower()

print(busquedaNombre)
    
email = archivos.buscarEmail(busquedaNombre)
if email:
    print(email)
else:
    print('Esa persona no se encuentra en la lista')