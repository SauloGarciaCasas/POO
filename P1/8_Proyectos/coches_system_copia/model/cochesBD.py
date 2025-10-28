from conexionBD import *

class Autos:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas

    def insertar(self):
        try:
            cursor.execute("INSERT INTO coches VALUES(null, %s, %s, %s, %s, %s, %s)", (self._marca, self._color, self._modelo, self._velocidad, self._caballaje, self._plazas))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM coches")
            return cursor.fetchall()
        except:    
            return []

    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, id):
        try:
            cursor.execute("UPDATE coches SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s WHERE id=%s", (marca, color, modelo, velocidad, caballaje, plazas, id))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM coches WHERE id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False

class Camionetas:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            cursor.execute("INSERT INTO camionetas VALUES(null, %s, %s, %s, %s, %s, %s, %s, %s)", (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camionetas")
            return cursor.fetchall()
        except:    
            return []
        
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id):
        try:
            cursor.execute("UPDATE camionetas SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, traccion=%s, cerrada=%s WHERE id=%s", (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM camionetas WHERE id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False

class Camiones:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        try:
            cursor.execute("INSERT INTO camiones VALUES(null, %s, %s, %s, %s, %s, %s, %s, %s)", (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camiones")
            return cursor.fetchall()
        except:    
            return []
        
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id):
        try:
            cursor.execute("UPDATE camiones SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, eje=%s, capacidadCarga=%s WHERE id=%s", (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM camiones WHERE id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False