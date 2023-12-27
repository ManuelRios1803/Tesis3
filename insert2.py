import pyodbc
import random


conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=DESKTOP-D5RJ734;"
                      "Database=TesisIII;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()

# Lista de nombres y apellidos para generar datos aleatorios
marcas = [
    "Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen", "Nissan", "BMW", "Mercedes-Benz",
    "Audi", "Hyundai", "Kia", "Mazda", "Subaru", "Lexus", "Jeep", "Tesla", "Ferrari", "Porsche",
    "Lamborghini", "Volvo", "Jaguar", "Land Rover", "Mini", "Buick", "Cadillac", "Chrysler"
]

# Lista de modelos de autos
modelos = [
    "Corolla", "Civic", "F-150", "Silverado", "Golf", "Sentra", "3 Series", "E-Class",
    "A4", "Elantra", "Optima", "CX-5", "Outback", "RX", "Wrangler", "Model S", "488", "911",
    "Huracan", "XC90", "F-Type", "Range Rover", "Cooper", "Enclave", "Escalade", "300"
]

# Lista de años de autos
anios = [
    "2015", "2018", "2019", "2018", "2019", "2020", "2018", "2019", "2020", "2020", "2016",
    "2018", "2019", "2020", "2017", "2018", "2019", "2018", "2019", "2020", "2020", "2021",
    "2022", "2015", "2012","2019"
]


# Número de registros que quieres insertar
num_registros = 1000

# Generar y ejecutar las sentencias SQL INSERT
for i in range(num_registros):
    numero_random = random.randint(0, 25)
    idAuto = i + 1  # Puedes usar alguna lógica para generar el idPersona si es necesario
    Marca = marcas[numero_random]
    Modelo = modelos[numero_random]
    Año = anios[numero_random]

    # Sentencia SQL INSERT
    sql_insert = f"INSERT INTO Auto (idAuto, Marca, Modelo, Año) VALUES (?, ?, ?, ?)"

    # Ejecutar la sentencia SQL con los valores correspondientes
    cursor.execute(sql_insert, (idAuto, Marca, Modelo, Año))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Tabla rellenada con éxito.")
