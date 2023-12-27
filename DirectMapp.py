from neo4j import GraphDatabase
from py2neo import Graph
import pyodbc
import time

#CREDENCIALES PARA NEO4J
uri = "bolt://localhost:7687"
usuario = "neo4j"
contrasena = "password"
conexion_neo4j = Graph(uri, auth=(usuario, contrasena))

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))


#CREDENCIALES PARA SQL SERVER
cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=DESKTOP-D5RJ734;"
                      "Database=TesisIII;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()

Inicio = time.time()

#SE EXTRAE LOS NOMBRES DE LAS TABLAS DE LA BASE DE DATOS TesisIII
cursor.execute("SELECT TABLE_NAME FROM information_schema.tables WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'dbo'")
curs = cursor.fetchall()
tabla = list()

# Imprimir los nombres de las tablas
for nombtab in curs:
    tabla.append(nombtab[0])
print(tabla)

#En esta sección vamos a proceder a separar las tablas que serán nodos y las tablas que serán relaciones
list_tabla_nodo=list()
list_tabla_relación=list()
#Iteramos en la lista tabla donde están todas las tablas y primero separamos las tablas que contengan el caracter '_' en su propio nombre
#Ya que sería indicio de que es una tabla relación ($NombreTabla_$NombreTabla) ejemplo Persona_Persona ó Persona_Auto.
for i in range(len(tabla)):
    if "_" in tabla[i]:
        list_tabla_relación.append(tabla[i])
    else :
        list_tabla_nodo.append(tabla[i])
print(list_tabla_nodo)
print(list_tabla_relación)

#SE ITERARÁ LA LISTA list_tabla_nodo PARA REALIZAR UN QUERY QUE EXTRAE LOS DATOS Y SE PROCEDERÁ A CREAR LOS NODOS
for i in range(len(list_tabla_nodo)):
    query = "Select * from " + list_tabla_nodo[i]
    cursor.execute(query)

    #Iteramos en los nombres de los atributos
    atributos = [atributo[0] for atributo in cursor.description]
    resultados = cursor.fetchall()
    
    #Iteramos en las filas
    for fila in resultados:

        queryneo4j = f"MERGE (n:{list_tabla_nodo[i]} "+ "{"f" {atributos[1]}:" + f"'{fila[1]}'"
        for j in range(2,len(atributos)):
            queryneo4j = queryneo4j + f", {atributos[j]}:" + f"'{fila[j]}'"
        queryneo4j = queryneo4j + f", {atributos[0]}:" + f"{fila[0]}"+"}) RETURN n" 
        
        print(queryneo4j)
        # Ejecutar la consulta dentro de una transacción
        with driver.session() as session:
            session.run(queryneo4j)
            
        #print(query)

######################################################################################################################################

#SE ITERARÁ LA LISTA list_tabla_relación PARA REALIZAR UN QUERY QUE EXTRAE LOS DATOS Y SE PROCEDERÁ A CREAR LAS RELACIONES
for i in range(len(list_tabla_relación)):
    query = "Select * from " + list_tabla_relación[i]
    cursor.execute(query)

    #Se itera en los nombres de los atributos
    atributosR = [atributo[0] for atributo in cursor.description]
    resultadosR = cursor.fetchall()
    
    #En esta sección como se tiene una tabla relación de personas tiene atributos idPersona1 e idPersona2 y a la hora de crear el query
    #de Neo4j se tendría "Match (n1 {idPersona1: 1}), (n2 {idPersona2: 2}) CREATE (n1)-[:relacion]->(n2)" por lo que estaría mal ya que
    #no debería de tener atributo idPersona1 e idPersona2 sino idPersona sin más.
    #Entonces de los atributos idPersona1 e idPersona2 se le elimina el 1 y el 2 respectivamente y se crea una condición if (stm1==stm2)
    st1 = atributosR[1]
    stm1 = st1[:-1]
    st2 = atributosR[2]
    stm2 = st2[:-1]

    #Aquí se codifica el code para la creación del query para la creación de relaciones con atributos idPersona1 e idPersona2 que serían
    #los atributos de la tabla Persona_Persona
    if (stm1==stm2):
        for fila in resultadosR:

            queryneo4j = f"Match (n1 " + "{" + f" {stm1}:" + f"{fila[1]}"+ "}), (n2 {" + f"{stm2}:" + f"{fila[2]}"+"}) " + "CREATE (n1)-[:"+ f"{fila[3]}" +"]->(n2)"
        
            print(queryneo4j)
            # Ejecutar la consulta dentro de una transacción
            with driver.session() as session:
                session.run(queryneo4j)
    
    #Aquí se codifica el code para la creación del query para la creación de relaciones con atributos diferentes como pro ejemplo
    #idPersona e idAuto, algo más general...
    else:
        for fila in resultadosR:
            queryneo4j = f"Match (n1 " + "{" + f" {atributosR[1]}:" + f"{fila[1]}"+ "}), (n2 {" + f"{atributosR[2]}:" + f"{fila[2]}"+"}) " + "CREATE (n1)-[:"+ f"{fila[3]}" +"]->(n2)"
        
            print(queryneo4j)
            # Ejecutar la consulta dentro de una transacción
            with driver.session() as session:
                session.run(queryneo4j)

Fin = time.time()

print("\nIntercambio de datos exitosa\n")
print ("Tiempo de ejecución: ", Fin-Inicio)

