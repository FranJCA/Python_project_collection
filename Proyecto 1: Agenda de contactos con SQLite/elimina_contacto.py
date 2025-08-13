def eliminar_contacto(id_contacto):
    conn = sqlite3.connect("agenda.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contactos WHERE id = ?", (id_contacto,))
    conn.commit()
    conn.close()

# Ejemplo
eliminar_contacto(1)
