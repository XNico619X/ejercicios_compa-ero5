class HotelVista:
    def __init__(self, controlador):
        self.controlador = controlador

    def mostrar_menu(self):
        print("\n=== Menú de Reserva de Hotel ===")
        print("1. Registrar reserva")
        print("2. Mostrar habitaciones disponibles")
        print("3. Consultar reservas realizadas")
        print("4. Cancelar una reserva")
        print("5. Salir")
        return input("Seleccione una opción: ")

    def solicitar_datos_reserva(self):
        nombre = self._leer_texto("Ingrese el nombre del cliente: ")
        numero_habitacion = self._leer_entero(
            "Ingrese el número de habitación (1-10): ", 1, 10)
        numero_noches = self._leer_entero(
            "Ingrese la cantidad de noches: ", 1, None)
        precio_noche = self._leer_flotante(
            "Ingrese el precio por noche: ", 0.01, None)
        return nombre, numero_habitacion, numero_noches, precio_noche

    def mostrar_habitaciones_disponibles(self, habitaciones):
        if not habitaciones:
            print("No hay habitaciones disponibles.")
        else:
            print("\n=== Habitaciones Disponibles ===")
            print("Habitaciones libres:", ", ".join(str(h)
                  for h in habitaciones))

    def mostrar_reservas(self, reservas):
        if not reservas:
            print("No hay reservas realizadas.")
            return

        print("\n=== Reservas Realizadas ===")
        for reserva in reservas:
            print(f"ID: {reserva['id']}, Cliente: {reserva['nombre']}, Habitación: {reserva['numero_habitacion']}, "
                  f"Noches: {reserva['numero_noches']}, Precio por noche: {reserva['precio_noche']:.2f}, Total: {reserva['total']:.2f}")

        total_general = sum(reserva['total'] for reserva in reservas)
        print(f"Valor total de todas las reservas: {total_general:.2f}")

    def solicitar_id_reserva(self):
        return self._leer_entero("Ingrese el ID de la reserva a cancelar: ", 1, None)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def _leer_texto(self, prompt):
        while True:
            texto = input(prompt).strip()
            if texto:
                return texto
            print("El dato no puede quedar vacío. Intente de nuevo.")

    def _leer_entero(self, prompt, minimo=None, maximo=None):
        while True:
            try:
                valor = int(input(prompt))
                if minimo is not None and valor < minimo:
                    print(f"El valor debe ser mayor o igual a {minimo}.")
                    continue
                if maximo is not None and valor > maximo:
                    print(f"El valor debe ser menor o igual a {maximo}.")
                    continue
                return valor
            except ValueError:
                print("Ingrese un número entero válido.")

    def _leer_flotante(self, prompt, minimo=None, maximo=None):
        while True:
            try:
                valor = float(input(prompt))
                if minimo is not None and valor < minimo:
                    print(f"El valor debe ser mayor o igual a {minimo}.")
                    continue
                if maximo is not None and valor > maximo:
                    print(f"El valor debe ser menor o igual a {maximo}.")
                    continue
                return valor
            except ValueError:
                print("Ingrese un número válido.")
