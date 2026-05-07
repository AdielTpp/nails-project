import sqlite3

def init_db():
    connection = sqlite3.connect('database.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute("INSERT INTO content (seccion_id, titulo, descripcion, precio, imagen_url) VALUES (?, ?, ?, ?, ?)",
                ('hero', 'Tus uñas, tu propio lienzo', 'Diseños únicos, creados por ti o por IA.', 0.0, ''))

    cur.execute("INSERT INTO content (seccion_id, titulo, descripcion, precio, imagen_url) VALUES (?, ?, ?, ?, ?)",
                ('catalog_item', 'Lavanda Glitter', 'Uñas lavanda con destellos plateados', 350.0, 'static/img/catalog1.png'))

    cur.execute("INSERT INTO content (seccion_id, titulo, descripcion, precio, imagen_url) VALUES (?, ?, ?, ?, ?)",
                ('catalog_item', 'Minimalist Nude', 'Diseño elegante con flores sutiles', 420.0, 'static/img/catalog2.png'))

    cur.execute("INSERT INTO content (seccion_id, titulo, descripcion, precio, imagen_url) VALUES (?, ?, ?, ?, ?)",
                ('catalog_item', 'Marble Dream', 'Efecto mármol con detalles en oro', 480.0, 'static/img/hero.png'))

    connection.commit()
    connection.close()
    print("Base de datos inicializada correctamente.")

if __name__ == '__main__':
    init_db()
