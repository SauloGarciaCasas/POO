import os
os.system("cls")

class Coches:
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.__marca = marca
        self.__color = color
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__caballaje = caballaje
        self.__plazas = plazas

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self.__velocidad = velocidad

    @property
    def caballaje(self):
        return self.__caballaje

    @caballaje.setter
    def caballaje(self, caballaje):
        self.__caballaje = caballaje

    @property
    def plazas(self):
        return self.__plazas

    @plazas.setter
    def plazas(self, plazas):
        self.__plazas = plazas

    def acelerar(self):
        return "Estás acelerando el coche"

    def frenar(self):
        return "Estás frenando el coche"


class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje = eje
        self.__capacidadCarga = capacidadCarga

    def cargar(self, tipo_carga):
        self.tipo_carga = tipo_carga
        return self.tipo_carga

    def acelerar(self):
        return "Estás acelerando el camión"

    def frenar(self):
        return "Estás frenando el camión"

    @property
    def eje(self):
        return self.__eje

    @eje.setter
    def eje(self, eje):
        self.__eje = eje

    @property
    def capacidadCarga(self):
        return self.__capacidadCarga

    @capacidadCarga.setter
    def capacidadCarga(self, capacidadCarga):
        self.__capacidadCarga = capacidadCarga


class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion = traccion
        self.__cerrada = cerrada

    def transportar(self, num_pasajeros):
        self.num_pasajeros = num_pasajeros
        return self.num_pasajeros

    def acelerar(self):
        return "Estás acelerando la camioneta"

    def frenar(self):
        return "Estás frenando la camioneta"

    @property
    def traccion(self):
        return self.__traccion

    @traccion.setter
    def traccion(self, traccion):
        self.__traccion = traccion

    @property
    def cerrada(self):
        return self.__cerrada

    @cerrada.setter
    def cerrada(self, cerrada):
        self.__cerrada = cerrada
