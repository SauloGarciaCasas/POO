from coches import *

num_coches = int(input("¿Cuántos coches tienes?: "))

for i in range(num_coches):
    print(f"\n\t ... Datos del coche {i+1} ...")
    marca = input("Ingresa la marca del auto: ").upper()
    color = input("Ingresa el color del auto: ").upper()
    modelo = input("Ingresa el modelo del auto: ").upper()
    velocidad = int(input("Ingresa la velocidad del auto: "))
    caballaje = int(input("Ingresa la potencia (caballaje) del auto: "))
    plazas = int(input("Ingresa las plazas del auto: "))

    coche = Coches(marca, color, modelo, velocidad, caballaje, plazas)

    print(f"""
    Datos del Vehículo:
      Marca: {coche.marca}
      Color: {coche.color}
      Modelo: {coche.modelo}
      Velocidad: {coche.velocidad}
      Potencia: {coche.caballaje}
      Plazas: {coche.plazas}
    """)

num_camiones = int(input("\n¿Cuántos camiones tienes?: "))

for i in range(num_camiones):
    print(f"\n\t ... Datos del camión {i+1} ...")
    marca = input("Ingresa la marca del camión: ").upper()
    color = input("Ingresa el color del camión: ").upper()
    modelo = input("Ingresa el modelo del camión: ").upper()
    velocidad = int(input("Ingresa la velocidad del camión: "))
    caballaje = int(input("Ingresa la potencia (caballaje) del camión: "))
    plazas = int(input("Ingresa las plazas del camión: "))
    eje = int(input("Número de ejes: "))
    capacidad = int(input("Capacidad de carga (kg): "))

    camion = Camiones(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad)

    print(f"""
    Datos del Camión:
      Marca: {camion.marca}
      Color: {camion.color}
      Modelo: {camion.modelo}
      Velocidad: {camion.velocidad}
      Potencia: {camion.caballaje}
      Plazas: {camion.plazas}
      Ejes: {camion.eje}
      Capacidad de carga: {camion.capacidadCarga} kg
    """)

num_camionetas = int(input("\n¿Cuántas camionetas tienes?: "))

for i in range(num_camionetas):
    print(f"\n\t ... Datos de la camioneta {i+1} ...")
    marca = input("Ingresa la marca de la camioneta: ").upper()
    color = input("Ingresa el color de la camioneta: ").upper()
    modelo = input("Ingresa el modelo de la camioneta: ").upper()
    velocidad = int(input("Ingresa la velocidad de la camioneta: "))
    caballaje = int(input("Ingresa la potencia (caballaje) de la camioneta: "))
    plazas = int(input("Ingresa las plazas de la camioneta: "))
    traccion = input("Tipo de tracción: ").upper()
    cerrada = input("¿Es cerrada? (SI/NO): ").upper()

    camioneta = Camionetas(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)

    print(f"""
    Datos de la Camioneta:
      Marca: {camioneta.marca}
      Color: {camioneta.color}
      Modelo: {camioneta.modelo}
      Velocidad: {camioneta.velocidad}
      Potencia: {camioneta.caballaje}
      Plazas: {camioneta.plazas}
      Tracción: {camioneta.traccion}
      Cerrada: {camioneta.cerrada}
    """)
