import hashlib

class Usuario:
    def __init__(self, nombre, apellidos, email, password):
       self._nombre = nombre
       self._apellidos = apellidos
       self._email = email
       self._password = self._hash_password(password)

    def _hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    @property
    def nombre(self):
       return self._nombre
    
    @property
    def apellidos(self):
       return self._apellidos
    
    @property
    def email(self):
       return self._email

    @property
    def password(self):
       return self._password

class Nota:
    def __init__(self, usuario_id, titulo, descripcion):
        self._usuario_id = usuario_id
        self._titulo = titulo
        self._descripcion = descripcion

    @property
    def usuario_id(self):
       return self._usuario_id

    @property
    def titulo(self):
       return self._titulo
    
    @titulo.setter
    def titulo(self, titulo):
       self._titulo = titulo

    @property
    def descripcion(self):
       return self._descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion):
       self._descripcion = descripcion