DROP TABLE IF EXISTS content;

CREATE TABLE content (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    seccion_id TEXT NOT NULL,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    precio REAL,
    imagen_url TEXT
);
