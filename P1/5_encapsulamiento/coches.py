import os
os.system("cls")

class Coches:
    #Método constructor para inicializar los valores de los atributos a la hora de crear o instanciar el objeto de la clase

    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
         self.__marca=marca
         self.__color=color
         self.__modelo=modelo
         self.__velocidad=velocidad
         self.__caballaje=caballaje
         self.__plazas=plazas
    
    """
    Crear los métodos setters y getters .- estos métodos son importantes y necesarios en todas las clases para que el programador interactue con los valores de los atributos 
    a través de estos métodos ... digamos que es la manera más adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atrubuto 
    en particular de la clase a través de un objeto.
    
    En teoría se debería de crear un método Getters y Setters por cada atributo que contenga la clase
    """
    #Primera forma

    def getMarca(self):
       return self.__marca
    
    def setMarca(self,Marca):
       self.__marca = Marca

    #Segunda forma
    @property
    def Marca2(self):
       return self.__marca
    
    @Marca2.setter
    def Marca2(self,marca):
       self.__marca = marca


    def getColor(self):
       return self.__color
    
    def setColor(self,Color):
       self.__color = Color

    def getModelo(self):
       return self.__modelo
    
    def setModelo(self,Modelo):
       self.__modelo = Modelo

    def getVelocidad(self):
       return self.__velocidad
    
    def setVelocidad(self,Velocidad):
       self.__velocidad = Velocidad
      
    def getCaballaje(self):
       return self.__caballaje
    
    def setCaballaje(self,Caballaje):
       self.__caballaje = Caballaje

    def getPlazas(self):
       return self.__plazas
    
    def setPlazas(self,Plazas):
       self.__plazas = Plazas


    def acelerar(self):
      return "Estas acelerando"

    def frenar(self):
      return "Estas frenando"  

#Fin definir clase
