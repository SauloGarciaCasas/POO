class fabrica:
    def __init__(self,llantas,color,precio):
        self._llantas=llantas
        self._color=color
        self._precio=precio

    @property
    def llantas(self):
        return self._llantas
    
    @llantas.setter
    def llantas(self, llantas):
        self._llantas=llantas

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color=color
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color=color

class moto(fabrica):
    def __init__(self,llantas,color,precio,tipo_moto):
        super().__init__(llantas,color,precio)
        self._tipo_moto=tipo_moto
    
    @property
    def tipo_moto(self):
        return self._tipo_moto
    
    @tipo_moto.setter
    def tipo_moto(self, tipo_moto):
        self._tipo_moto=tipo_moto

class carro(fabrica):
    def __init__(self,llantas,color,precio,tipo_carro):
        super().__init__(llantas,color,precio)
        self._tipo_carro=tipo_carro
    
    @property
    def tipo_carro(self):
        return self._tipo_carro
    
    @tipo_carro.setter
    def tipo_carro(self, tipo_carro):
        self._tipo_carro=tipo_carro

moto1=moto(2, "Rojo", 12000, "Sport")
carro1=carro(4, "Azul", 100000, "Sedan")

print(moto1.color, moto1.llantas, moto1.tipo_moto)