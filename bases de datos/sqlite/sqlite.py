import sqlite3

# Conexion
conexion = sqlite3.connect("pruebas.db")

# Crear cursor (permite ejecutar consultas)
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS futbolistas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(255),
        edad int(255),
        posicion VARCHAR(255)
    )
""")

# Guardar cambios
conexion.commit()

# Insertar datos
"""
cursor.execute("INSERT INTO futbolistas VALUES (null, 'Chupete', 35, 'delantero')")
conexion.commit()
"""

# Borrar datos
cursor.execute("DELETE FROM futbolistas")
conexion.commit()

# Insertar muchos datos
futbolistas = [('Chupete', 35, 'delantero'), ('Mago Jimenez', 50, 'delantero'),
               ('Xupete', 35, 'delantero')]
cursor.executemany("INSERT INTO futbolistas VALUES (null, ?, ?, ?)",
                   futbolistas)
conexion.commit()

# Leer datos
cursor.execute("SELECT * FROM futbolistas")
futbolistas = cursor.fetchall()
print(futbolistas)

cursor.execute("SELECT * FROM futbolistas")
futbolista = cursor.fetchone()  # Obtiene el primer registro
print(futbolista)

# Actualizar datos
cursor.execute("UPDATE futbolistas SET edad=40 WHERE edad > 35")

cursor.execute("SELECT * FROM futbolistas")
futbolistas = cursor.fetchall()
print(futbolistas)

# Cerrar conexion
conexion.close()
