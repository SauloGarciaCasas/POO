#Instanciar los objetos para posterior implementarlos 
from model import coches, cochesBD
import os

def borrarPantalla():
    os.system("cls")

def espereTecla():
    input("Oprima una tecla para continuar...")

def respuesta_sql(respuesta):
    if respuesta:
        print("Acción realizada con éxito")
        espereTecla()
    else:
        input("No fue posible realizar la acción, vuelva a intentar...")

def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("No. de plazas: "))
    return marca,color,modelo,velocidad,potencia,plazas

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,potencia,plazas):
    print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n color: {color} \n Modelo: {modelo} \n velocidad: {velocidad} \n caballaje: {potencia} \n plazas: {plazas}")

def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
    coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
    borrarPantalla()
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas
    

def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camioneta")
    traccion=input("Traccion: ").upper()
    cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False    
    coche=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")
    return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.traccion,coche.cerrada

def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camiones")
    eje=int(input("No. de ejes: "))
    capacidadCarga=int(input("Capacidad de carga: "))
    coche=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")
    return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.eje,coche.capacidadCarga

def menu_acciones(tipo):
    print(f"\n\t ...Menú de {tipo} ::. \n\t1.- Insertar\n\t2.- Consultar\n\t3.- Actualizar\n\t4.- Eliminar\n\t5.- Regresar")
    opcion = input("\n\t\t Elige una opción: ").upper().strip()
    return opcion

def menu_autos():
    while True:
        borrarPantalla()
        opcion = menu_acciones("Autos")
        if opcion == "1" or opcion == "INSERTAR":
            marca,color,modelo,velocidad,caballaje,plazas = autos()
            #Agregar el registro a la BD
            auto=cochesBD.Autos(marca, color, modelo, velocidad, caballaje, plazas)
            respuesta=auto.insertar()
            respuesta_sql(respuesta)
        elif opcion == "2" or opcion == "CONSULTAR":
            borrarPantalla()
            registros = cochesBD.Autos.consultar()
            if len(registros)>0:
                num_autos=1
                for fila in registros:
                    print(f"Auto # {num_autos} con ID: {fila[0]}\nMarca: {fila[1]}\nColor: {fila[2]}\nModelo: {fila[3]}\nVelocidad: {fila[4]}\nPotencia: {fila[5]}\nPlazas: {fila[6]}")
                    num_autos+=1
                    espereTecla()
            else:
                print("...No hay datos que mostrar por el momento")
                espereTecla()
        elif opcion == "3" or opcion == "ACTUALIZAR":
            borrarPantalla()
            id=input("Ingrese el ID a actualizar: ").strip()
            marca,color,modelo,velocidad,caballaje,plazas = autos()
            respuesta=cochesBD.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
            respuesta_sql(respuesta)
        elif opcion == "4" or opcion == "ELIMINAR":
            borrarPantalla()
            id=input("Ingrese el ID a eliminar: ").strip()
            respuesta=cochesBD.Autos.eliminar(id)
            respuesta_sql(respuesta)
        elif opcion == "5" or opcion == "REGRESAR":
            break
        else:
            input("\n\t\t Opción no válida... Vuelve a intentar... ")

def menu_camionetas():
    while True:
        borrarPantalla()
        opcion = menu_acciones("Camionetas")
        if opcion == "1" or opcion == "INSERTAR":
            marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada = camionetas()
            respuesta = cochesBD.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
            respuesta_sql(respuesta)
        elif opcion == "2" or opcion == "CONSULTAR":
            borrarPantalla()
            registros = cochesBD.Camionetas.consultar()
            if len(registros)>0:
                num_camioneta=1
                for fila in registros:
                    print(f"Camioneta # {num_camioneta} con ID: {fila[0]}\nMarca: {fila[1]}\nColor: {fila[2]}\nModelo: {fila[3]}\nVelocidad: {fila[4]}\nPotencia: {fila[5]}\nPlazas: {fila[6]}\nTraccion: {fila[7]}\nCerrada: {fila[8]}")
                    num_camioneta+=1
                    espereTecla()
            else:
                print("...No hay datos que mostrar por el momento")
                espereTecla()
        elif opcion == "3" or opcion == "ACTUALIZAR":
            borrarPantalla()
            id=input("Ingrese el ID a actualizar: ").strip()
            marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada = camionetas()
            respuesta=cochesBD.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
            respuesta_sql(respuesta)
        elif opcion == "4" or opcion == "ELIMINAR":
            borrarPantalla()
            id=input("Ingrese el ID a eliminar: ").strip()
            respuesta=cochesBD.Camionetas.eliminar(id)
            respuesta_sql(respuesta)
        elif opcion == "5" or opcion == "REGRESAR":
            break
        else:
            input("\n\t\t Opción no válida... Vuelve a intentar... ")

def menu_camiones():
    while True:
        borrarPantalla()
        opcion = menu_acciones("Camiones")
        if opcion == "1" or opcion == "INSERTAR":
            marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga = camiones()
            respuesta = cochesBD.Camiones.insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
            respuesta_sql(respuesta)
        elif opcion == "2" or opcion == "CONSULTAR":
            borrarPantalla()
            registros = cochesBD.Camiones.consultar()
            if len(registros)>0:
                num_camion=1
                for fila in registros:
                    print(f"Camión # {num_camion} con ID: {fila[0]}\nMarca: {fila[1]}\nColor: {fila[2]}\nModelo: {fila[3]}\nVelocidad: {fila[4]}\nPotencia: {fila[5]}\nPlazas: {fila[6]}\nEje: {fila[7]}\nCapacidadCarga: {fila[8]}")
                    num_camion+=1
                    espereTecla()
            else:
                print("...No hay datos que mostrar por el momento")
                espereTecla()
        elif opcion == "3" or opcion == "ACTUALIZAR":
            borrarPantalla()
            id=input("Ingrese el ID a actualizar: ").strip()
            marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga = camiones()
            respuesta=cochesBD.Camiones.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
            respuesta_sql(respuesta)
        elif opcion == "4" or opcion == "ELIMINAR":
            borrarPantalla()
            id=input("Ingrese el ID a eliminar: ").strip()
            respuesta=cochesBD.Camiones.eliminar(id)
            respuesta_sql(respuesta)
        elif opcion == "5" or opcion == "REGRESAR":
            break
        else:
            input("\n\t\t Opción no válida... Vuelve a intentar... ")

def main():
    opcion=True
    while opcion:
        borrarPantalla()
        opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.- Autos\n\t2.- Camionetas\n\t3.- Camiones\n\t4.- Salir\n\tElige un opción: ").lower().strip()
        match opcion:
            case "1":
                menu_autos()
            case "2":
                menu_camionetas()
            case "3":
                menu_camiones()
            case "4":
                print("Saliste del Sistema..")
                opcion=False   
            case _:
                input("Opcion invalida ... vuelva a intertarlo ... ")      

if __name__=="__main__":
    main()
