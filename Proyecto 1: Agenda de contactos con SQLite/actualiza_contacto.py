
def actualizar_contacto(id_contacto, nuevo_telefono):
    conn = sqlite3.connect("agenda.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contactos SET telefono = ? WHERE id = ?", (nuevo_telefono, id_contacto))
    conn.commit()
    conn.close()

# Ejemplo
actualizar_contacto(1, "987654321")
