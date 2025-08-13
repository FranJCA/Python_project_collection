def listar_contactos():
    conn = sqlite3.connect("agenda.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos")
    for fila in cursor.fetchall():
        print(fila)
    conn.close()

# Ejemplo
listar_contactos()
