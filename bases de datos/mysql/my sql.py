# Primero es necesario tener el modulo conector de mysql para python
import mysql.connector

# Conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

# Crear cursor (permite ejecutar consultas)
cursor = database.cursor()

# Crear database
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

"""
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)
"""

# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS futbolistas(
        id INTEGER PRIMARY KEY auto_increment,
        nombre VARCHAR(255),
        edad int(255),
        posicion VARCHAR(255)
    )
""")

"""
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
"""

# Insertar datos
cursor.execute("INSERT INTO futbolistas VALUES (null, 'Chupete', 35, 'delantero')")
database.commit()

# Borrar datos
cursor.execute("DELETE FROM futbolistas")
database.commit()

# Insertar muchos datos
futbolistas = [
    ('Chupete', 35, 'delantero'),
    ('Mago Jimenez', 50, 'delantero'),
    ('Xupete', 35, 'delantero')
]
cursor.executemany("INSERT INTO futbolistas VALUES (null, %s, %s, %s)",
                   futbolistas)
database.commit()

# Leer datos
cursor.execute("SELECT * FROM futbolistas")
futbolistas = cursor.fetchall()
print(futbolistas)

"""
cursor.execute("SELECT * FROM futbolistas")
futbolista = cursor.fetchone()  # Obtiene el primer registro
print(futbolista)
"""

# Actualizar datos
cursor.execute("UPDATE futbolistas SET edad = 40 WHERE edad > 35")
database.commit()

cursor.execute("SELECT * FROM futbolistas")
futbolistas = cursor.fetchall()
print(futbolistas)

# Cerrar conexion
database.close()