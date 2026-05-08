import sqlite3

# Tu lista de productos personalizada
mis_productos = [
    {"titulo": "Lavanda Glitter", "descripcion": "Uñas lavanda con destellos plateados", "precio": 350.0, "imagen_url": "static/img/catalog1.png"},
    {"titulo": "Minimalist Nude", "descripcion": "Diseño elegante con flores sutiles", "precio": 420.0, "imagen_url": "static/img/catalog2.png"},
    {"titulo": "French Celeste", "descripcion": "Uñas francesas color celeste pastel", "precio": 450.0, "imagen_url": "static/img/catalog3.png"},
    {"titulo": "Marble Dream", "descripcion": "Efecto mármol con detalles en oro", "precio": 480.0, "imagen_url": "static/img/hero.png"},
    {"titulo": "Kawaii Pastel", "descripcion": "Estética suave y juguetona", "precio": 80.0, "imagen_url": "static/img/catalog4.png"},
    {"titulo": "Kawaii Pastel", "descripcion": "Estética suave y juguetona", "precio": 80.0, "imagen_url": "static/img/catalog5.png"},
    {"titulo": "Kawaii Pastel", "descripcion": "Estética suave y juguetona", "precio": 80.0, "imagen_url": "static/img/catalog6.png"}
]

def init_db():
    connection = sqlite3.connect('database.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    # Hero content
    cur.execute("INSERT INTO content (seccion_id, titulo, descripcion, precio, imagen_url) VALUES (?, ?, ?, ?, ?)",
                ('hero', 'Press-On Nails Premium', 'Diseños únicos hechos a mano para resaltar tu estilo.', 0.0, ''))

    # Insertar tus productos desde la lista
    for p in mis_productos:
        cur.execute("INSERT INTO content (seccion_id, titulo, descripcion, precio, imagen_url) VALUES (?, ?, ?, ?, ?)",
                    ('catalog_item', p['titulo'], p['descripcion'], p['precio'], p['imagen_url']))

    connection.commit()
    connection.close()
    print("Base de datos actualizada con tus nuevos productos.")

if __name__ == '__main__':
    init_db()
