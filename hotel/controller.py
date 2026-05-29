from model import HotelReservas
from vista import HotelVista


class HotelControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == '1':
                self.registrar_reserva()
            elif opcion == '2':
                self.mostrar_habitaciones_disponibles()
            elif opcion == '3':
                self.consultar_reservas()
            elif opcion == '4':
                self.cancelar_reserva()
            elif opcion == '5':
                self.vista.mostrar_mensaje("Saliendo del sistema...")
                break
            else:
                self.vista.mostrar_mensaje(
                    "Opción no válida. Intente de nuevo.")

    def registrar_reserva(self):
        nombre, numero_habitacion, numero_noches, precio_noche = self.vista.solicitar_datos_reserva()
        try:
            self.modelo.agregar_reserva(
                nombre, numero_habitacion, numero_noches, precio_noche)
            self.vista.mostrar_mensaje("Reserva registrada con éxito.")
        except ValueError as error:
            self.vista.mostrar_mensaje(str(error))

    def mostrar_habitaciones_disponibles(self):
        disponibles = self.modelo.habitaciones_disponibles()
        self.vista.mostrar_habitaciones_disponibles(disponibles)

    def consultar_reservas(self):
        reservas = self.modelo.listar_reservas()
        self.vista.mostrar_reservas(reservas)

    def cancelar_reserva(self):
        reserva_id = self.vista.solicitar_id_reserva()
        try:
            self.modelo.cancelar_reserva(reserva_id)
            self.vista.mostrar_mensaje("Reserva cancelada con éxito.")
        except ValueError as error:
            self.vista.mostrar_mensaje(str(error))
