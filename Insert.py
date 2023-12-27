import pyodbc
import random

conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=DESKTOP-D5RJ734;"
                      "Database=TesisIII;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()

# Lista de nombres y apellidos para generar datos aleatorios
nombres = [
    "Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Charlotte", "William", "Sophia",
    "James", "Amelia", "Benjamin", "Isabella", "Lucas", "Mia", "Henry", "Evelyn", "Alexander", "Harper",
    "Michael", "Abigail", "Daniel", "Emily", "Ethan", "Elizabeth", "Matthew", "Sofia", "Joseph", "Avery",
    "David", "Ella", "Mason", "Scarlett", "Logan", "Grace", "Jackson", "Chloe", "Samuel", "Victoria",
    "Sebastian", "Riley", "Jack", "Aria", "Aiden", "Lily", "Owen", "Aurora", "Gabriel", "Hannah",
    "Carter", "Layla", "John", "Zoey", "Luke", "Penelope", "Anthony", "Nora", "Isaac", "Addison",
    "Dylan", "Bella", "Wyatt", "Camila", "Andrew", "Luna", "Joshua", "Stella", "Christopher", "Maya",
    "Grayson", "Skylar", "Eli", "Hazel", "Isaiah", "Savannah", "Joseph", "Natalie", "Levi", "Emilia"
]

apellidos = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Taylor", "Clark",
    "Martinez", "Anderson", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White", "Lopez",
    "Lee", "Gonzalez", "Harris", "Robinson", "Lewis", "Walker", "Perez", "Hall", "Young", "Allen",
    "Sanchez", "Wright", "King", "Scott", "Green", "Baker", "Adams", "Nelson", "Hill", "Ramirez",
    "Campbell", "Mitchell", "Roberts", "Carter", "Phillips", "Evans", "Turner", "Torres", "Parker", "Collins",
    "Edwards", "Stewart", "Flores", "Morris", "Nguyen", "Murphy", "Rivera", "Cook", "Rogers", "Morgan",
    "Peterson", "Cooper", "Reed", "Bailey", "Bell", "Gomez", "Kelly", "Howard", "Ward", "Cox",
    "Diaz", "Richardson", "Wood", "Watson", "Brooks", "Bennett", "Gray", "James", "Reyes", "Cruz"
]

# Número de registros que quieres insertar
num_registros = 1000

# Generar y ejecutar las sentencias SQL INSERT
for i in range(num_registros):
    idPersona = i + 1  # Puedes usar alguna lógica para generar el idPersona si es necesario
    nombrePersona = random.choice(nombres)
    apellidoPersona = random.choice(apellidos)

    # Sentencia SQL INSERT
    sql_insert = f"INSERT INTO Persona (idPersona, nombrePersona, apellidoPersona) VALUES (?, ?, ?)"

    # Ejecutar la sentencia SQL con los valores correspondientes
    cursor.execute(sql_insert, (idPersona, nombrePersona, apellidoPersona))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Tabla rellenada con éxito.")
