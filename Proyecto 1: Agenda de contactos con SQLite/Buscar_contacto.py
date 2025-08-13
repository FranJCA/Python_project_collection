
def buscar_contacto(nombre):
    conn = sqlite3.connect("agenda.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos WHERE nombre LIKE ?", ('%' + nombre + '%',))
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conn.close()

# Ejemplo
buscar_contacto("Juan")
