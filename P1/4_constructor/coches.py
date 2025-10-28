import os
os.system("cls")

class Coches:
    #Método constructor para inicializar los valores de los atributos a la hora de crear o instanciar el objeto de la clase

    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
         self.marca=marca
         self.color=color
         self.modelo=modelo
         self.velocidad=velocidad
         self.caballaje=caballaje
         self.plazas=plazas
    
    """
    Crear los métodos setters y getters .- estos métodos son importantes y necesarios en todas las clases para que el programador interactue con los valores de los atributos 
    a través de estos métodos ... digamos que es la manera más adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atrubuto 
    en particular de la clase a través de un objeto.
    
    En teoría se debería de crear un método Getters y Setters por cada atributo que contenga la clase
    """
    #Primera forma

    def getMarca(self):
       return self.marca
    
    def setMarca(self,Marca):
       self.marca = Marca

    #Segunda forma
    @property
    def Marca2(self):
       return self.marca
    
    @Marca2.setter
    def Marca2(self,marca):
       self.marca = marca


    def getColor(self):
       return self.color
    
    def setColor(self,Color):
       self.color = Color

    def getModelo(self):
       return self.modelo
    
    def setModelo(self,Modelo):
       self.modelo = Modelo

    def getVelocidad(self):
       return self.velocidad
    
    def setVelocidad(self,Velocidad):
       self.velocidad = Velocidad
      
    def getCaballaje(self):
       return self.caballaje
    
    def setCaballaje(self,Caballaje):
       self.caballaje = Caballaje

    def getPlazas(self):
       return self.plazas
    
    def setPlazas(self,Plazas):
       self.plazas = Plazas


    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase
coche1=Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
coche3=Coches("Honda", "", "", 0, 0, 0)
coche1.num_serie="B014567890"
coche4=Coches("", "", "", 0, 0, 0)
coche4.marca2="Volvo"
print(coche4.Marca2)

print(f"Datos del Vehiculo 1: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n numero de serie: {coche1.num_serie} ")

print(f"\nDatos del Vehiculo 2: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

print(coche3.Marca2)

#coche1.marca="VW"
#coche1.color="Blanco"
#coche1.modelo="2022"
#coche1.velocidad=220
#coche1.caballaje=150
#coche1.plazas=5

#coche2.marca="Nissan"
#coche2.color="Azul"
#coche2.modelo="2020"
#coche2.velocidad=180
#coche2.caballaje=150
#coche2.plazas=6