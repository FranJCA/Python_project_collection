def agregar_contacto(nombre, telefono, email):
    conn = sqlite3.connect("agenda.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contactos (nombre, telefono, email) VALUES (?, ?, ?)", (nombre, telefono, email))
    conn.commit()
    conn.close()

# Ejemplo
agregar_contacto("Juan Pérez", "123456789", "juan@example.com")


def agregar_conmtaco( nombre, telefono email):
    conn = sqlite.connet("agenda.db")