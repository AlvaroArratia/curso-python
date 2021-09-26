from tkinter import *
import os.path


class Programa:

    def __init__(self):
        self.title = "GRACIAS MASTER"
        self.icon = './imagenes/rayo.ico'
        self.icon_alt = './tkinter/imagenes/rayo.ico'
        self.size = "750x550"
        self.resizable = False
        self.ventana = Tk()  # Crear ventana raiz

    def cargar(self):

        # Cambiar titulo
        self.ventana.title(self.title)

        # Agregado
        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Mostrar texto en el programa
        texto = Label(self.ventana, text=ruta_icono)
        texto.pack()

        # Icono de ventana
        self.ventana.iconbitmap(self.icon)

        # Cambio de tamaño de ventana
        self.ventana.geometry(self.size)

        # Bloquear tamaño
        if self.resizable:
            self.ventana.resizable(1, 1)
        else:
            self.ventana.resizable(0, 0)

    def agregar_texto(self, texto):
        label = Label(self.ventana, text=texto)
        label.pack()

    def mostrar(self):
        # Arrancar y mostrar ventana
        self.ventana.mainloop()


ventana = Programa()

ventana.cargar()

ventana.agregar_texto("AASDUYUJLASDAS")
ventana.agregar_texto("AAAFGHAAAASDAS")
ventana.agregar_texto("ANMAHJFGAASDAS")

ventana.mostrar()
