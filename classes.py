import threading
import time
import random
from queue import Queue

t = 15
n = 1


class Coche(threading.Thread):

    def __init__(self, nombre):
        threading.Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        Surtidor(1, self.nombre).start()

class Surtidor(threading.Thread):

    def __init__(self, nombre, coche):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.coche = coche

    def run(self):
        print("Surtidor %s: %s ha llegado" % (self.nombre, self.coche))
        time.sleep(random.randint(5, 10))
        print("Surtidor %s: %s ha terminado" % (self.nombre, self.coche))
        
class Gasolinera(threading.Thread):
    
    def __init__(self, nombre, coche):
            threading.Thread.__init__(self)
            self.nombre = nombre
            self.coche = coche
            self.cola = Queue()
    
    def coche_entra_fila(self):
        self.cola.put(self.coche)
        print("El conductor del Coche %s se pone en la fila" % self.coche.nombre)

    def coche_sale_fila(self):
        time.sleep(3)
        print("El conductor del Coche %s ha pagado" % self.coche.nombre)
        self.cola.get()

    def run(self):
        self.coche_entra_fila()
        self.coche_sale_fila()

def generar_coche():
    for i in range(50):
        coche = Coche("Coche %s" % i)
        coche.start()
        time.sleep(15)

#def generar_surtidor():
 #   for i in range(n):
  #      surtidor = Surtidor("Surtidor %s" % i, coche)
   #     surtidor.start()

if __name__ == "__main__":
    generar_coche()
    #generar_surtidor()
