import sqlite3


class ModeloTorneo:
    def __init__(self, db_name='torneo_videojuegos.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jugadores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                videojuego TEXT NOT NULL,
                puntaje INTEGER NOT NULL DEFAULT 0
            )
        ''')
        self.conn.commit()

    def agregar_jugador(self, nombre, videojuego, puntaje_inicial=0):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO jugadores (nombre, videojuego, puntaje) VALUES (?, ?, ?)',
                (nombre, videojuego, puntaje_inicial)
            )
            self.conn.commit()
            return True, cursor.lastrowid
        except Exception as e:
            return False, str(e)

    def obtener_jugadores(self):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT id, nombre, videojuego, puntaje FROM jugadores ORDER BY id')
        return cursor.fetchall()

    def actualizar_puntaje(self, jugador_id, puntos):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT puntaje FROM jugadores WHERE id = ?', (jugador_id,))
        resultado = cursor.fetchone()
        if resultado is None:
            return False, 'No existe un jugador con el ID proporcionado.'

        puntaje_actual = resultado[0]
        nuevo_puntaje = puntaje_actual + puntos
        cursor.execute(
            'UPDATE jugadores SET puntaje = ? WHERE id = ?', (nuevo_puntaje, jugador_id))
        self.conn.commit()
        return True, nuevo_puntaje

    def obtener_ranking(self):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT id, nombre, videojuego, puntaje FROM jugadores ORDER BY puntaje DESC, nombre ASC')
        return cursor.fetchall()

    def buscar_por_nombre(self, nombre):
        cursor = self.conn.cursor()
        termino = f'%{nombre}%'
        cursor.execute(
            'SELECT id, nombre, videojuego, puntaje FROM jugadores WHERE nombre LIKE ? COLLATE NOCASE ORDER BY id',
            (termino,)
        )
        return cursor.fetchall()

    def cerrar_conexion(self):
        self.conn.close()
