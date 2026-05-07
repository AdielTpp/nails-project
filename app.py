from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey_presson_nails' # Para futuras sesiones de login

DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    catalog = conn.execute('SELECT * FROM content WHERE seccion_id = "catalog_item"').fetchall()
    hero = conn.execute('SELECT * FROM content WHERE seccion_id = "hero"').fetchone()
    conn.close()
    return render_template('index.html', catalog=catalog, hero=hero)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
