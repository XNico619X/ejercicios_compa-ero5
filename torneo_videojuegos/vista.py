import tkinter as tk
from tkinter import ttk, messagebox


class VistaTorneo:
    def __init__(self, root):
        self.root = root
        self.root.title('Torneo de Videojuegos')

        self.frame_form = ttk.Frame(self.root, padding=16)
        self.frame_form.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.frame_form, text='Nombre del jugador:').grid(
            row=0, column=0, sticky=tk.W)
        self.entry_nombre = ttk.Entry(self.frame_form, width=30)
        self.entry_nombre.grid(row=0, column=1, padx=4, pady=4)

        ttk.Label(self.frame_form, text='Videojuego favorito:').grid(
            row=1, column=0, sticky=tk.W)
        self.entry_videojuego = ttk.Entry(self.frame_form, width=30)
        self.entry_videojuego.grid(row=1, column=1, padx=4, pady=4)

        ttk.Label(self.frame_form, text='Puntaje inicial:').grid(
            row=2, column=0, sticky=tk.W)
        self.entry_puntaje = ttk.Entry(self.frame_form, width=30)
        self.entry_puntaje.grid(row=2, column=1, padx=4, pady=4)
        self.entry_puntaje.insert(0, '0')

        self.btn_registrar_jugador = ttk.Button(
            self.frame_form, text='Registrar jugador')
        self.btn_registrar_jugador.grid(
            row=3, column=0, columnspan=2, pady=(8, 12), sticky=(tk.W, tk.E))

        ttk.Separator(self.root, orient='horizontal').grid(
            row=1, column=0, sticky=(tk.W, tk.E), pady=8)

        self.frame_score = ttk.Frame(self.root, padding=16)
        self.frame_score.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.frame_score, text='ID del jugador:').grid(
            row=0, column=0, sticky=tk.W)
        self.entry_id_jugador = ttk.Entry(self.frame_score, width=15)
        self.entry_id_jugador.grid(row=0, column=1, padx=4, pady=4)

        ttk.Label(self.frame_score, text='Puntos ganados:').grid(
            row=1, column=0, sticky=tk.W)
        self.entry_puntos = ttk.Entry(self.frame_score, width=15)
        self.entry_puntos.grid(row=1, column=1, padx=4, pady=4)

        self.btn_actualizar_puntaje = ttk.Button(
            self.frame_score, text='Registrar puntaje')
        self.btn_actualizar_puntaje.grid(
            row=2, column=0, columnspan=2, pady=(8, 12), sticky=(tk.W, tk.E))

        ttk.Separator(self.root, orient='horizontal').grid(
            row=3, column=0, sticky=(tk.W, tk.E), pady=8)

        self.frame_busqueda = ttk.Frame(self.root, padding=16)
        self.frame_busqueda.grid(
            row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.frame_busqueda, text='Buscar por nombre:').grid(
            row=0, column=0, sticky=tk.W)
        self.entry_buscar = ttk.Entry(self.frame_busqueda, width=30)
        self.entry_buscar.grid(row=0, column=1, padx=4, pady=4)
        self.btn_buscar_nombre = ttk.Button(
            self.frame_busqueda, text='Buscar jugador')
        self.btn_buscar_nombre.grid(row=0, column=2, padx=(8, 0), pady=4)

        self.btn_mostrar_jugadores = ttk.Button(
            self.frame_busqueda, text='Mostrar jugadores')
        self.btn_mostrar_jugadores.grid(
            row=1, column=0, columnspan=2, pady=(8, 4), sticky=(tk.W, tk.E))

        self.btn_mostrar_ranking = ttk.Button(
            self.frame_busqueda, text='Mostrar ranking')
        self.btn_mostrar_ranking.grid(
            row=1, column=2, pady=(8, 4), sticky=(tk.W, tk.E))

        self.btn_salir = ttk.Button(self.frame_busqueda, text='Salir')
        self.btn_salir.grid(row=2, column=0, columnspan=3,
                            pady=(8, 0), sticky=(tk.W, tk.E))

        self.frame_tabla = ttk.Frame(self.root, padding=16)
        self.frame_tabla.grid(row=5, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.tabla_jugadores = ttk.Treeview(self.frame_tabla, columns=(
            'ID', 'Nombre', 'Videojuego', 'Puntaje'), show='headings', height=10)
        self.tabla_jugadores.heading('ID', text='ID')
        self.tabla_jugadores.heading('Nombre', text='Nombre')
        self.tabla_jugadores.heading('Videojuego', text='Videojuego')
        self.tabla_jugadores.heading('Puntaje', text='Puntaje')
        self.tabla_jugadores.column('ID', width=50, anchor=tk.CENTER)
        self.tabla_jugadores.column('Nombre', width=170)
        self.tabla_jugadores.column('Videojuego', width=170)
        self.tabla_jugadores.column('Puntaje', width=100, anchor=tk.CENTER)
        self.tabla_jugadores.pack(fill=tk.BOTH, expand=True)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(5, weight=1)

    def obtener_datos_jugador(self):
        nombre = self.entry_nombre.get().strip()
        videojuego = self.entry_videojuego.get().strip()
        puntaje = self.entry_puntaje.get().strip()
        return nombre, videojuego, puntaje

    def obtener_datos_puntaje(self):
        jugador_id = self.entry_id_jugador.get().strip()
        puntos = self.entry_puntos.get().strip()
        return jugador_id, puntos

    def obtener_termino_busqueda(self):
        return self.entry_buscar.get().strip()

    def mostrar_jugadores(self, jugadores):
        for item in self.tabla_jugadores.get_children():
            self.tabla_jugadores.delete(item)
        for jugador in jugadores:
            self.tabla_jugadores.insert('', 'end', values=jugador)

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_videojuego.delete(0, tk.END)
        self.entry_puntaje.delete(0, tk.END)
        self.entry_puntaje.insert(0, '0')
        self.entry_id_jugador.delete(0, tk.END)
        self.entry_puntos.delete(0, tk.END)
        self.entry_buscar.delete(0, tk.END)
