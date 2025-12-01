import math

class Figuras:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible
    
    def estaVisible(self):
        return self.visible
    
    def mostrar(self):
        self.visible = True
        print(f"La figura en ({self.x}, {self.y}) ahora es visible.")
    
    def ocultar(self):
        self.visible = False
        print(f"La figura en ({self.x}, {self.y}) ahora está oculta.")
    
    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
        print(f"La figura se ha movido a ({self.x}, {self.y}).")
        
    def calcularArea(self):
        raise NotImplementedError("El método 'calcularArea' debe ser implementado por las subclases.")


class Rectangulos(Figuras):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.__alto = alto
        self.__ancho = ancho
    
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        self.__alto = alto

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho
        
    def ocultar(self):
        self.visible = False
        print(f"El rectángulo ({self.x}, {self.y}) está oculto.")

    def mostrar(self):
        self.visible = True
        print(f"El rectángulo ({self.x}, {self.y}) es visible.")
    
    def calcularArea(self):
        return float(self.__alto * self.__ancho)


class Circulos(Figuras):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self.__radio = radio

    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, radio):
        self.__radio = radio

    def ocultar(self):
        self.visible = False
        print(f"El círculo ({self.x}, {self.y}) está oculto.")

    def mostrar(self):
        self.visible = True
        print(f"El círculo ({self.x}, {self.y}) es visible.")

    def calcularArea(self):
        return float(math.pi * (self.__radio ** 2))


rectangulo1 = Rectangulos(3, 4, True, 10, 20)
circulo1 = Circulos(3, 3, True, 6)

print("\n--- Pruebas ---")
print(f"Área de rectangulo1: {rectangulo1.calcularArea()}")
print(f"Área de circulo1: {circulo1.calcularArea()}")

rectangulo1.mover(5, 5)
circulo1.ocultar()
print(f"Visibilidad de circulo1: {circulo1.estaVisible()}")