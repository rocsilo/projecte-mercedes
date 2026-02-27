import mysql.connector

# ---------------------------------------------------------
# 1. CONEXIÓN A LA BASE DE DATOS 'mails'
# ---------------------------------------------------------
try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="mal"     # <--- Tu base de datos
    )
    mycursor = mydb.cursor()

    # ---------------------------------------------------------
    # 2. TU FUNCIÓN buscarEmail ADAPTADA
    # ---------------------------------------------------------
    def buscarEmail(busquedaNombre):
        # Traducimos tu lógica a SQL:
        # "Dame el Gmail (COL2) de la tabla 'nom_email' DONDE el Nombre (COL1) sea..."
        sql = "SELECT mail FROM nom_email WHERE nom = %s"
        
        val = (busquedaNombre, )

        try:
            mycursor.execute(sql, val)
            resultado = mycursor.fetchone() # Obtiene el primer resultado

            if resultado:
                # resultado es una tupla ej: ('diego@example.com',)
                return resultado[0] # Devolvemos COL2
            else:
                return None
                
        except mysql.connector.Error as err:
            print(f"Error buscando datos: {err}")
            return None

    # ---------------------------------------------------------
    # 3. PRUEBA DE FUNCIONAMIENTO
    # ---------------------------------------------------------
    nombre_a_buscar = "Diego"
    email_encontrado = buscarEmail(nombre_a_buscar)

    if email_encontrado:
        print(f"✅ ¡ENCONTRADO! El email de {nombre_a_buscar} es: {email_encontrado}")
    else:
        print(f"❌ No se encontró a '{nombre_a_buscar}' en la tabla 'nom_email'.")
        print("Verifica que hayas metido datos en COL 1 y COL 2.")

    # Cerramos conexión al final
    mydb.close()

except mysql.connector.Error as err:
    print(f"❌ ERROR DE CONEXIÓN: {err}")
    print("Asegúrate de que la base de datos 'mails' existe.")