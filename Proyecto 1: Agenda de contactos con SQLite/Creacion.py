import sqlite3

# Conectar (si no existe el archivo, se crea)
conn = sqlite3.connect("agenda.db")
cursor = conn.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS contactos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    email TEXT
)
""")

conn.commit()
conn.close()
