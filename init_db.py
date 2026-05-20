import sqlite3

# Tu lista de productos personalizada con nombres y descripciones profesionales
mis_productos = [
    {"titulo": "Lavanda Glitter", "descripcion": "Elegantes uñas en tono lavanda profundo con una lluvia de destellos plateados iridiscentes. El set perfecto para una noche de gala.", "precio": 200.0, "imagen_url": "static/img/hero.png"},
    {"titulo": "Minimalist Nude", "descripcion": "Base nude sofisticada decorada con micro-flores artesanales. Un diseño atemporal que aporta limpieza y elegancia a tus manos.", "precio": 200.0, "imagen_url": "static/img/catalog1.png"},
    {"titulo": "French Celeste", "descripcion": "Una reinvención del clásico francés en tono celeste pastel. Ideal para un look fresco, juvenil y altamente estético.", "precio": 200.0, "imagen_url": "static/img/catalog2.png"},
    {"titulo": "Gengar Nails", "descripcion": "Estilo stiletto con acabado artístico hecho a mano alzada, inspirado en los Pokémon de tipo fantasma más icónicos. Oscuridad y estilo en uno.", "precio": 200.0, "imagen_url": "static/img/catalog3.png"},
    {"titulo": "Kawaii Starter Squad", "descripcion": "Set de colección inspirado en los iniciales de Kanto. Retratos minuciosos de Pikachu, Charmander y Squirtle con acabados de alto brillo.", "precio": 220.0, "imagen_url": "static/img/catalog4.png"},
    {"titulo": "Pastel Dream Garden", "descripcion": "Estética soft-girl con relieves 3D de cerezas, nubes y margaritas. Un diseño juguetón que evoca la frescura de un jardín primaveral.", "precio": 120.0, "imagen_url": "static/img/catalog5.png"},
    {"titulo": "Amethyst Dreams", "descripcion": "Tonos lavanda y violeta con aplicaciones de corazones y estrellas. El set ideal para un look soñador, mágico y lleno de personalidad.", "precio": 120.0, "imagen_url": "static/img/catalog6.png"},
    {"titulo": "Celestial Crescent", "descripcion": "Degradados pastel con detalles de lunas y estrellas en relieve dorado. Un diseño místico que captura la esencia del cielo nocturno.", "precio": 120.0, "imagen_url": "static/img/catalog7.jpg"},
    {"titulo": "Spirited Away Art", "descripcion": "Homenaje artístico a Studio Ghibli. Retratos detallados de Sin Cara y el Espíritu del Río sobre un acabado mate de lujo.", "precio": 200.0, "imagen_url": "static/img/catalog8.jpg"},
    {"titulo": "Totoro Blue Shimmer", "descripcion": "Elegante diseño de Totoro sobre base celeste con destellos iridiscentes y finas líneas doradas trazadas a mano.", "precio": 150.0, "imagen_url": "static/img/catalog9.jpg"},
    {"titulo": "Starry Night Minimalist", "descripcion": "Contraste sofisticado en blanco y negro con estrellas fugaces y cristales incrustados. Un clásico moderno impecable.", "precio": 120.0, "imagen_url": "static/img/catalog10.jpg"},
    {"titulo": "Pochacco Sky Blue", "descripcion": "Diseño adorable de Pochacco en azul cielo con espirales hipnóticas y estrellas plateadas. Estética pura y divertida.", "precio": 180.0, "imagen_url": "static/img/catalog11.jpg"},
    {"titulo": "Vulpix Seasons Duo", "descripcion": "Dúo dinámico de Vulpix (Kanto y Alola) con patrones de cuadros escoceses y copos de nieve. Versatilidad y estilo Pokémon.", "precio": 200.0, "imagen_url": "static/img/catalog12.jpg"},
    {"titulo": "Porcelain Halloween", "descripcion": "Halloween exclusivo estilo porcelana azul. Calaveras y castillos con un nivel de detalle artístico superior y único.", "precio": 200.0, "imagen_url": "static/img/catalog13.jpg"},
    {"titulo": "Sweet Paw Portraits", "descripcion": "Nude cálido con ilustraciones tiernas de cachorros y gatitos. Acabado acogedor con patrones de cuadros y lazos clásicos.", "precio": 120.0, "imagen_url": "static/img/catalog14.jpg"},
    {"titulo": "Witchy Midnight Blue", "descripcion": "Azul marino profundo con simbología mística: libélulas, arañas y constelaciones. Para almas magnéticas y misteriosas.", "precio": 200.0, "imagen_url": "static/img/catalog15.jpg"},
    {"titulo": "Starry Ribbon Azure", "descripcion": "Lazos elegantes y espirales infinitas sobre fondo azul estelar. El equilibrio perfecto entre ternura y sofisticación moderna.", "precio": 180.0, "imagen_url": "static/img/catalog16.jpg"},
    {"titulo": "Royal Blue Jewels", "descripcion": "Ombré azul real con aplicaciones de cristales tipo diamante y detalles dorados. Un set digno de una celebración de gala.", "precio": 250.0, "imagen_url": "static/img/catalog17.jpg"},
    {"titulo": "Cyber Bunny Teal", "descripcion": "Fondo teal profundo con corazones cromados en 3D y conejitos futuristas. Una mezcla audaz de vanguardia y ternura.", "precio": 200.0, "imagen_url": "static/img/catalog18.jpg"},
    {"titulo": "Punk Rock Plaid", "descripcion": "Estilo alternativo con calaveras, cuadros grises y perlas plateadas. Refleja tu lado rebelde con una elegancia impecable.", "precio": 220.0, "imagen_url": "static/img/catalog19.jpg"},
    {"titulo": "Woodstock Starry Night", "descripcion": "Snoopy y Woodstock bajo una noche estrellada. Diseño limpio con lazos 3D y perlas que aportan volumen y lujo extremo.", "precio": 240.0, "imagen_url": "static/img/catalog20.jpg"},
    {"titulo": "Winter Wonderland 3D", "descripcion": "Escultura en uñas con muñecos de nieve y esferas navideñas en 3D real. La magia de las fiestas en cada detalle táctil.", "precio": 250.0, "imagen_url": "static/img/catalog21.jpg"},
    {"titulo": "Frozen Reindeer Luxury", "descripcion": "Elegancia invernal en blanco y azul. Detalles de renos plateados, perlas y texturas acolchadas de alta costura.", "precio": 250.0, "imagen_url": "static/img/catalog22.jpg"},
    {"titulo": "Espeon & Umbreon Tarot", "descripcion": "Cartas del tarot inspiradas en las evoluciones de Eevee. Simbolismo astral con un acabado artístico digno de museo.", "precio": 180.0, "imagen_url": "static/img/catalog23.jpg"},
    {"titulo": "Snowflake Serenity", "descripcion": "Árboles y copos de nieve sobre azul gélido brillante. Un diseño que transmite la paz y pureza de la primera nevada.", "precio": 250.0, "imagen_url": "static/img/catalog24.jpg"},
    {"titulo": "Orca Ocean Waves", "descripcion": "Arte fluido inspirado en el movimiento de las orcas. Base iridiscente que simula el reflejo del sol sobre el océano.", "precio": 250.0, "imagen_url": "static/img/catalog25.jpg"},
    {"titulo": "Deep Sea Biolume", "descripcion": "Manta rayas y tiburones ballena en aguas profundas. Gotas de agua 3D que crean una experiencia sensorial única.", "precio": 250.0, "imagen_url": "static/img/catalog26.jpg"},
    {"titulo": "Snoopy Christmas Joy", "descripcion": "El clásico Snoopy con luces de colores y bastones de caramelo. Un set lleno de alegría nostálgica y festiva.", "precio": 160.0, "imagen_url": "static/img/catalog27.jpg"},
    {"titulo": "Let It Snow Texture", "descripcion": "Texturas de suéter de lana en 3D con copos de nieve y Snoopy invernal. Máxima calidez y detalle en tu manicura.", "precio": 250.0, "imagen_url": "static/img/catalog28.jpg"},
    {"titulo": "Glowing Coral Reef", "descripcion": "Tortugas y medusas con efectos de luminiscencia submarina. Verdes y azules profundos que cobran vida bajo la luz.", "precio": 220.0, "imagen_url": "static/img/catalog29.jpg"},
    {"titulo": "Ghostly Purple Squad", "descripcion": "Pokémon tipo fantasma sobre un lienzo púrpura místico. Mimikyu y Litwick detallados con sombreado profesional.", "precio": 220.0, "imagen_url": "static/img/catalog30.jpg"},
    {"titulo": "Melody Celestial", "descripcion": "Sinfonía de estrellas y notas musicales sobre degradado amatista. Para las amantes de la música y el arte estelar.", "precio": 250.0, "imagen_url": "static/img/catalog31.jpg"},
    {"titulo": "Emerald Serpent", "descripcion": "Serpientes místicas pintadas a mano entre follaje esmeralda y gemas preciosas. Un diseño audaz, potente y lujoso.", "precio": 200.0, "imagen_url": "static/img/catalog32.jpg"},
    {"titulo": "High Fantasy Crest", "descripcion": "Escudos y emblemas dorados sobre azul imperial. Inspirado en leyendas épicas con un acabado de joyería fina.", "precio": 200.0, "imagen_url": "static/img/catalog33.jpg"},
    {"titulo": "Delft Totoro Blue", "descripcion": "Fusión de Totoro con el arte de la cerámica de Delft. Flores azules y blancas con un toque clásico y atemporal.", "precio": 240.0, "imagen_url": "static/img/catalog34.jpg"},
    {"titulo": "Melodic Cat Onyx", "descripcion": "Gatitos musicales y pentagramas en blanco y negro. Un diseño minimalista, tierno y lleno de ritmo visual.", "precio": 100.0, "imagen_url": "static/img/catalog35.jpg"},
    {"titulo": "Straw Hat Crew 3D", "descripcion": "La tripulación de Luffy en relieve 3D. Fuego, mar e iconografía pirata para los verdaderos fans de One Piece.", "precio": 250.0, "imagen_url": "static/img/catalog36.jpg"},
    {"titulo": "Poseidon's Treasure", "descripcion": "Tesoros marinos en relieve: tridentes, pulpos y conchas con acabados holográficos y perlas naturales.", "precio": 250.0, "imagen_url": "static/img/catalog37.jpg"},
    {"titulo": "Celestial Cloud Gold", "descripcion": "Lunas y estrellas bañadas en oro sobre un cielo nublado etéreo. Un diseño que parece sacado de un sueño lúcido.", "precio": 20.0, "imagen_url": "static/img/catalog38.jpg"},
    {"titulo": "Fire Fist Ace Tribute", "descripcion": "Tributo a Ace con llamas intensas y retratos hiperrealistas. El espíritu de los piratas de Spade en tus manos.", "precio": 220.0, "imagen_url": "static/img/catalog39.jpg"},
    {"titulo": "Sun God Nika Edition", "descripcion": "Gear 5 de Luffy con efectos de nubes 3D y detalles de los nakamas. Un set de nivel coleccionista premium.", "precio": 250.0, "imagen_url": "static/img/catalog40.jpg"},
    {"titulo": "Heart Pirates Stealth", "descripcion": "Inspirado en Trafalgar Law. Brújulas, mapas antiguos y el corazón de Corazón en un estilo sobrio y poderoso.", "precio": 250.0, "imagen_url": "static/img/catalog41.jpg"},
    {"titulo": "Wonderland Tea Party", "descripcion": "Alicia en el País de las Maravillas. Relojes locos, la Reina de Corazones y engranajes steampunk detallados.", "precio": 250.0, "imagen_url": "static/img/catalog42.jpg"},
    {"titulo": "Stained Glass Cat", "descripcion": "Gato negro sobre una luna de vitral. Colores vibrantes y líneas doradas que resplandecen. Una joya gótica moderna.", "precio": 200.0, "imagen_url": "static/img/catalog43.jpg"},
    {"titulo": "Dreamy Kirby Pink", "descripcion": "Kirby explorando mundos de algodón de azúcar. Brillos estelares y el rosa más vibrante para un look ultra kawaii.", "precio": 150.0, "imagen_url": "static/img/catalog44.jpg"},
    {"titulo": "Mystic Cat Stars", "descripcion": "Ojos que todo lo ven y siluetas de gatos entre las estrellas. Azul místico con trazos blancos ultra finos de precisión.", "precio": 200.0, "imagen_url": "static/img/catalog45.jpg"},
    {"titulo": "Soul Eater Academy", "descripcion": "Inspirado en Soul Eater. Lord Death y Soul Evans en un estilo dark shonen con negros y violetas profundos.", "precio": 180.0, "imagen_url": "static/img/catalog46.jpg"},
    {"titulo": "Starry Ribbon Sky", "descripcion": "Gatitos blancos jugando con la luna sobre azul degradado. Lazos plateados y perlas para un toque dulce y lujoso.", "precio": 180.0, "imagen_url": "static/img/catalog47.jpg"},
    {"titulo": "Steve & Friends Pixel", "descripcion": "Minimalismo pixelado de Minecraft. Steve, Alex y Creepers con acabados brillantes que resaltan cada bloque.", "precio": 120.0, "imagen_url": "static/img/catalog48.jpg"},
    {"titulo": "Pixel Adventure Set", "descripcion": "Iconos clásicos de Minecraft en pixel art: espada de diamante y ajolotes. Diversión retro, colorida y detallada.", "precio": 150.0, "imagen_url": "static/img/catalog49.jpg"},
    {"titulo": "Cinnamoroll Marine", "descripcion": "Cinnamoroll y medusas flotando en un mar de frescura. Helados y estrellas que completan este set ultra tierno y chic.", "precio": 200.0, "imagen_url": "static/img/catalog50.jpg"}
]

def init_db():
    connection = sqlite3.connect('database.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    # Hero content
    cur.execute("INSERT INTO content (seccion_id, titulo, descripcion, precio, imagen_url) VALUES (?, ?, ?, ?, ?)",
                ('hero', 'Press-On Nails Premium', 'Diseños únicos hechos a mano para resaltar tu estilo con lujo y elegancia.', 0.0, ''))

    # Insertar tus productos desde la lista
    for p in mis_productos:
        cur.execute("INSERT INTO content (seccion_id, titulo, descripcion, precio, imagen_url) VALUES (?, ?, ?, ?, ?)",
                    ('catalog_item', p['titulo'], p['descripcion'], p['precio'], p['imagen_url']))

    connection.commit()
    connection.close()
    print("Base de datos actualizada con tus nuevos productos y descripciones profesionales.")

if __name__ == '__main__':
    init_db()
