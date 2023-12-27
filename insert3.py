import pyodbc
import random


conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=DESKTOP-D5RJ734;"
                      "Database=TesisIII;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()

# Número de registros que quieres insertar
num_registros = 1000

# Generar y ejecutar las sentencias SQL INSERT
for i in range(num_registros):
    numero_random = random.randint(0, 25)
    idPersona_Auto = i + 1  # Puedes usar alguna lógica para generar el idPersona si es necesario
    idPersona = i + 1
    idAuto = i + 1
    relacionPA = "Conduce_un"

    # Sentencia SQL INSERT
    sql_insert = f"INSERT INTO Persona_Auto (idPersona_Auto, idPersona, idAuto, relacionPA) VALUES (?, ?, ?, ?)"

    # Ejecutar la sentencia SQL con los valores correspondientes
    cursor.execute(sql_insert, (idPersona_Auto, idPersona, idAuto, relacionPA))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Tabla rellenada con éxito.")
