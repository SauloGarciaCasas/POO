class Marino:
    def hablar(self):
        return "Hola ..."
    
class Pulpo(Marino):
    def hablar(self):
        return "Soy un pulpo"
    
class Foca(Marino):
    def __init__(self, mensaje):
        self._mensaje=mensaje

    @property
    def mensaje(self):
        return self._mensaje
    
    @mensaje.setter
    def mensaje(self, mensaje):
        self._mensaje = mensaje

foca1=Foca("Soy una foca")
print(foca1._mensaje)