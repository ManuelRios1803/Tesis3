import pyodbc
import random


conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=DESKTOP-D5RJ734;"
                      "Database=TesisIII;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()

rela = [
    "Conoce", "Amigo_de", "Trabaja_para", "Hermano_de", "Estudiante_de", "Profesor_de", "Manager_de", "Compañero_de", "Director_de",
    "Hijo_de", "Padre_de", "Jefe_de", "Vecino_de", "Casero_de", "Cocinero_de", "Ayudante_de", "Enemigo_de", "Coach_de", "Amante_de",
    "Pareja_de"
]

# Número de registros que quieres insertars
num_registros = 1000


# Generar y ejecutar las sentencias SQL INSERT
for i in range(num_registros):
    numero_random = random.randint(0, 19)
    number = random.randint(1, 1000)

    if (num_registros != number):
        idPersona_Persona = i + 1  # Puedes usar alguna lógica para generar el idPersona si es necesario
        idPersona1 = i + 1
        idPersona2 = number
        relacionPP = rela[numero_random]

        # Sentencia SQL INSERT
        sql_insert = f"INSERT INTO Persona_Persona (idPersona_Persona, idPersona1, idPersona2, relacionPP) VALUES (?, ?, ?, ?)"

        # Ejecutar la sentencia SQL con los valores correspondientes
        cursor.execute(sql_insert, (idPersona_Persona, idPersona1, idPersona2, relacionPP))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Tabla rellenada con éxito.")
