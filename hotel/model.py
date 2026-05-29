import sqlite3


class HotelReservas:
    def __init__(self, db_name='hotel_reservas.db'):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.habitaciones = list(range(1, 11))
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            numero_habitacion INTEGER NOT NULL,
            numero_noches INTEGER NOT NULL,
            precio_noche REAL NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def agregar_reserva(self, nombre, numero_habitacion, numero_noches, precio_noche):
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre del cliente no puede estar vacío.")
        if numero_habitacion not in self.habitaciones:
            raise ValueError(
                "El número de habitación debe estar entre 1 y 10.")
        if self.esta_ocupada(numero_habitacion):
            raise ValueError(
                f"La habitación {numero_habitacion} ya está ocupada.")
        if numero_noches <= 0:
            raise ValueError("La cantidad de noches debe ser mayor que cero.")
        if precio_noche <= 0:
            raise ValueError("El precio por noche debe ser mayor que cero.")

        query = '''
            INSERT INTO reservas (nombre, numero_habitacion, numero_noches, precio_noche)
            VALUES (?, ?, ?, ?)
        '''
        self.conn.execute(query, (nombre, numero_habitacion,
                          numero_noches, precio_noche))
        self.conn.commit()

    def esta_ocupada(self, numero_habitacion):
        query = 'SELECT 1 FROM reservas WHERE numero_habitacion = ?'
        cursor = self.conn.execute(query, (numero_habitacion,))
        return cursor.fetchone() is not None

    def habitaciones_disponibles(self):
        query = 'SELECT numero_habitacion FROM reservas'
        cursor = self.conn.execute(query)
        ocupadas = {row['numero_habitacion'] for row in cursor.fetchall()}
        return [h for h in self.habitaciones if h not in ocupadas]

    def listar_reservas(self):
        query = 'SELECT * FROM reservas'
        cursor = self.conn.execute(query)
        reservas_con_total = []
        for row in cursor.fetchall():
            reserva = dict(row)
            reserva['total'] = reserva['numero_noches'] * \
                reserva['precio_noche']
            reservas_con_total.append(reserva)
        return reservas_con_total

    def cancelar_reserva(self, reserva_id):
        query = 'DELETE FROM reservas WHERE id = ?'
        cursor = self.conn.execute(query, (reserva_id,))
        self.conn.commit()
        if cursor.rowcount == 0:
            raise ValueError(f"No existe una reserva con ID {reserva_id}.")
