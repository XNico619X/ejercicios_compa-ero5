import tkinter as tk
from controlador import ControladorTorneo


def main():
    root = tk.Tk()
    app = ControladorTorneo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
