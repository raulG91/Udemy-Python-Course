import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios " \
    "(nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

conexion.commit()

conexion.close()