import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios " \
    "(nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

#cursor.execute("INSERT INTO usuarios VALUES ('Hector', 27, 'hector@ejemplo.com')")
cursor.execute("SELECT * FROM usuarios")

usuario = cursor.fetchone()
print(usuario)


conexion.commit()

conexion.close()