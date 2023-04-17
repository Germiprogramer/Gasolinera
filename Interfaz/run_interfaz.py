from classes_interfaz import Coche, Surtidor, Gasolinera, Interfaz
import time
import random
from queue import Queue
import tkinter as tk

cola = Queue()
t = 15
n = 4

class Interfaz:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gasolinera")
        self.ventana.geometry("600x600")
        self.generar_surtidores()
        self.ventana.mainloop()

    def generar_surtidores(self):
        for i in range(n-1):
            surtidor = Surtidor("Surtidor %s" % i, self.ventana, 100, 100)
            surtidor.start()

def generar_coche():
    for i in range(50):
        coche = Coche("Coche %s" % i, random.randint(0,3), Gasolinera("Gasolinera","Coche %s" % i, cola))
        coche.start()
        time.sleep(t)

if __name__ == "__main__":
    generar_coche()
    Interfaz()