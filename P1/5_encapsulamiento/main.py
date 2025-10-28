from coches import *

#Solicitar los datos que posteriormente serajnlos atributos del objeto

num_coches = int(input("¿Cuantos coches tienes?: "))

for i in range (0, num_coches):
    print("\n\t ... Datos del automovil ...")
    marca = input("Ingresa la marca del auto: ").upper()
    color = input("Ingresa el color del auto: ").upper()
    modelo = input("Ingresa el modelo del auto: ").upper()
    velocidad = int(input("Ingresa la velocidad del auto: "))
    potencia = int(input("Ingresa la potencia del auto: "))
    plazas = int(input("Ingresa las plazas del auto: "))

    coche1 = Coches(marca, color, modelo, velocidad, potencia, plazas)

    print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n potencia: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}")

#coche1=Coches("VW", "Blanco", "2022", 220, 150, 5)
#coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
#coche3=Coches("Honda", "", "", 0, 0, 0)
#coche1.num_serie="B014567890"
#coche4=Coches("", "", "", 0, 0, 0)
#coche4.marca2="Volvo"
#print(coche4.Marca2)

#print(f"\nDatos del Vehiculo 2: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

#print(coche3.Marca2)