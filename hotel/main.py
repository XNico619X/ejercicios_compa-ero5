from model import HotelReservas
from vista import HotelVista
from controller import HotelControlador

if __name__ == "__main__":
    modelo = HotelReservas()
    vista = HotelVista(controlador=None)
    controlador = HotelControlador(modelo, vista)
    controlador.ejecutar()
