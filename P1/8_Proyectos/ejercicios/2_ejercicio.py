"""
Realizar un programa en el cual se declaren dos valores enteros por teclado. Calcular después de la suma, resta, multiplicación y división.
Utilizar el método constructor, así como los métodos para cada una e impromir los resultados obtenidos. llamar al la clase Calculadora.

"""

class Calculadora:
    def __init__(self, n1, n2):
        self._n1 = n1
        self._n2 = n2

    def sumar(self):
        return self._n1+self._n2
    
    def restar(self):
        return self._n1-self._n2
    
    def multiplicar(self):
        return self._n1*self._n2
    
    def dividir(self):
        return self._n1/self._n2
    

n1=int(input("Numero 1: "))
n2=int(input("Numero 2: "))
operacion = Calculadora(n1, n2)
print(operacion.sumar())
print(operacion.restar())
print(operacion.multiplicar())
print(operacion.dividir())