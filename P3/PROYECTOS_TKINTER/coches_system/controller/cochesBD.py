import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexionBD import *

class Autos:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas):
        try:
            sql = "INSERT INTO coches (marca, color, modelo, velocidad, caballaje, plazas) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (marca, color, modelo, velocidad, caballaje, plazas)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar Auto: {e}")
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM coches")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar Autos: {e}")
            return []

    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, id):
        try:
            sql = "UPDATE coches SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s WHERE id=%s"
            val = (marca, color, modelo, velocidad, caballaje, plazas, id)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar Auto: {e}")
            return False

    @staticmethod
    def eliminar(id):
        try:
            sql = "DELETE FROM coches WHERE id=%s"
            cursor.execute(sql, (id,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar Auto: {e}")
            return False       

class Camionetas:  
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            sql = "INSERT INTO camionetas (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar Camioneta: {e}")
            return False
    
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camionetas")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar Camionetas: {e}")
            return []

    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id):
        try:
            sql = "UPDATE camionetas SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, traccion=%s, cerrada=%s WHERE id_camionetas=%s"
            val = (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar Camioneta: {e}")
            return False

    @staticmethod
    def eliminar(id):
        try:
            sql = "DELETE FROM camionetas WHERE id_camionetas=%s"
            cursor.execute(sql, (id,))
            conexion.commit()
            return True  
        except Exception as e:
            print(f"Error al eliminar Camioneta: {e}")
            return False  

class Camiones: 
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        try:
            sql = "INSERT INTO camiones (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar Camión: {e}")
            return False
    
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camiones")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar Camiones: {e}")
            return []

    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id):
        try:
            sql = "UPDATE camiones SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, eje=%s, capacidadCarga=%s WHERE id_camion=%s"
            val = (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar Camión: {e}")
            return False

    @staticmethod
    def eliminar(id):
        try:
            sql = "DELETE FROM camiones WHERE id_camion=%s"
            cursor.execute(sql, (id,))
            conexion.commit() 
            return True  
        except Exception as e:
            print(f"Error al eliminar Camión: {e}")
            return False