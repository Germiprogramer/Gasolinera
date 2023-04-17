import threading
import time
import random
from queue import Queue
from threading import Semaphore
import tkinter as tk

class Coche(threading.Thread):

    def __init__(self, nombre, surtidor, gasolinera):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.surtidor = Surtidor(surtidor, self.nombre)
        self.gasolinera = gasolinera

    def run(self):
        self.surtidor.start()
        self.surtidor.join()
        self.gasolinera.start()
        self.gasolinera.join()

class Surtidor(threading.Thread):

    def __init__(self, nombre, coche, interfaz, x, y):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.coche = coche
        self.estado = "Libre"
        self.semaforo = Semaphore(1)
        self.interfaz = interfaz
        self.x = x
        self.y = y
        self.surtidor_grafico = tk.Label(self.interfaz, text=f"Surtidor {self.nombre} : {self.estado}")
        self.surtidor_grafico.place(x=self.x, y=self.y)
        self.coche_grafico = tk.Label(self.interfaz, text=f"{self.coche}")
        self.coche_grafico.place(x=self.x, y=self.y+20)

    def run(self):
        print("Surtidor %s: %s ha llegado" % (self.nombre, self.coche))
        self.semaforo.acquire()
        self.estado = "Ocupado"
        time.sleep(random.randint(5, 10))
        print("Surtidor %s: %s ha terminado" % (self.nombre, self.coche))
        self.estado = "Libre"
        self.semaforo.release()
        
class Gasolinera(threading.Thread):
    
    def __init__(self, nombre, coche, cola):
            threading.Thread.__init__(self)
            self.nombre = nombre
            self.coche = coche
            self.cola = cola
    
    def coche_entra_fila(self):
        self.cola.put(self.coche)
        print("El conductor del %s se pone en la fila" % self.coche)

    def coche_sale_fila(self):
        time.sleep(3)
        print("El conductor del %s ha pagado" % self.coche)
        self.cola.get()

    def run(self):
        self.coche_entra_fila()
        self.coche_sale_fila()

def generar_coche():
    for i in range(50):
        coche = Coche("Coche %s" % i)
        coche.start()
        time.sleep(10)

class Interfaz:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gasolinera")
        self.ventana.geometry("600x600")
        self.ventana.mainloop()
        