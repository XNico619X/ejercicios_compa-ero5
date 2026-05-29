from model import ModeloTorneo
from vista import VistaTorneo


class ControladorTorneo:
    def __init__(self, root):
        self.modelo = ModeloTorneo()
        self.vista = VistaTorneo(root)

        self.vista.btn_registrar_jugador.config(command=self.registrar_jugador)
        self.vista.btn_actualizar_puntaje.config(
            command=self.registrar_puntaje)
        self.vista.btn_mostrar_jugadores.config(command=self.mostrar_jugadores)
        self.vista.btn_mostrar_ranking.config(command=self.mostrar_ranking)
        self.vista.btn_buscar_nombre.config(command=self.buscar_jugador)
        self.vista.btn_salir.config(command=self.cerrar_aplicacion)

        self.mostrar_jugadores()
        root.protocol('WM_DELETE_WINDOW', self.cerrar_aplicacion)

    def registrar_jugador(self):
        nombre, videojuego, puntaje = self.vista.obtener_datos_jugador()
        if not nombre or not videojuego:
            self.vista.mostrar_mensaje('Error', 'Ingrese nombre y videojuego.')
            return

        try:
            puntaje_inicial = int(puntaje)
            if puntaje_inicial < 0:
                raise ValueError
        except ValueError:
            self.vista.mostrar_mensaje(
                'Error', 'El puntaje inicial debe ser un número entero mayor o igual a 0.')
            return

        exito, resultado = self.modelo.agregar_jugador(
            nombre, videojuego, puntaje_inicial)
        if exito:
            self.vista.mostrar_mensaje(
                'Éxito', f'Jugador registrado con ID: {resultado}')
            self.vista.limpiar_campos()
            self.mostrar_jugadores()
        else:
            self.vista.mostrar_mensaje('Error', resultado)

    def registrar_puntaje(self):
        jugador_id, puntos = self.vista.obtener_datos_puntaje()
        if not jugador_id or not puntos:
            self.vista.mostrar_mensaje(
                'Error', 'Ingrese el ID del jugador y los puntos a sumar.')
            return

        try:
            jugador_id = int(jugador_id)
            puntos = int(puntos)
            if puntos < 0:
                raise ValueError
        except ValueError:
            self.vista.mostrar_mensaje(
                'Error', 'ID y puntos deben ser números enteros válidos, y los puntos no pueden ser negativos.')
            return

        exito, resultado = self.modelo.actualizar_puntaje(jugador_id, puntos)
        if exito:
            self.vista.mostrar_mensaje(
                'Éxito', f'Puntaje actualizado. Nuevo puntaje: {resultado}')
            self.vista.limpiar_campos()
            self.mostrar_jugadores()
        else:
            self.vista.mostrar_mensaje('Error', resultado)

    def mostrar_jugadores(self):
        jugadores = self.modelo.obtener_jugadores()
        self.vista.mostrar_jugadores(jugadores)

    def mostrar_ranking(self):
        jugadores = self.modelo.obtener_ranking()
        self.vista.mostrar_jugadores(jugadores)

    def buscar_jugador(self):
        termino = self.vista.obtener_termino_busqueda()
        if not termino:
            self.vista.mostrar_mensaje(
                'Error', 'Ingrese un nombre para buscar.')
            return

        jugadores = self.modelo.buscar_por_nombre(termino)
        if jugadores:
            self.vista.mostrar_jugadores(jugadores)
        else:
            self.vista.mostrar_mensaje(
                'Información', 'No se encontró ningún jugador con ese nombre.')

    def cerrar_aplicacion(self):
        self.modelo.cerrar_conexion()
        self.vista.root.destroy()
