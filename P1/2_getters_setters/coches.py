import os
os.system("cls")

class Coches:
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0
    
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
coche1=Coches()
coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)


coche2=Coches()
coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)

print(f"Datos del Vehiculo 1: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")

print(f"\nDatos del Vehiculo 2: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

coche3=Coches()
coche3.marca2="Honda"
print(coche3.marca2)

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