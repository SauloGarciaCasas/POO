import os
os.system("cls")

class Alumno:
    def __init__(self, nombre, edad, matricula):
        self._nombre = nombre
        self._edad = edad
        self._matricula = matricula

    def inscribirse():
        return "El alumno se ha inscrito"
    
    def estudiar():
        return "El alumno está estudiando"

class Profesor:
    def __init__(self, nombre, experiencia, num_profesor):
        self._nombre = nombre
        self._experiencia = experiencia
        self._num_profesor = num_profesor

    def impartir():
        return "El profesor ha empezado a impartir"
    
    def evaluar():
        return "Se ha evaluado al profesor"

class Curso:
    def __init__(self, nombre, codigo, creditos):
        self._nombre = nombre
        self._codigo = codigo
        self._creditos = creditos

    def asignar():
        return "Se ha asignado el curso"


alumno1=Alumno("Diego", 18, "BHJB12211BJJH")
alumno2=Alumno("Alberto", 18, "UI32UI12FD23R")

profesor1=Profesor("Jaime", "Intermedio", 9)
profesor2=Profesor("Pablo", "Avanzado", 7)

curso1=Curso("Matematicas", "sdqw55", 135)
curso2=Curso("Programacion", "fs6ed7", 135)

print(f"El nombre del alumno 1 es: {alumno1._nombre}, su edad es de {alumno1._edad} y su matricula es: {alumno1._matricula}. Estatus: {Alumno.inscribirse()}")
print(f"\nEl nombre del alumno 2 es: {alumno2._nombre}, su edad es de {alumno2._edad} y su matricula es: {alumno2._matricula}. Estatus: {Alumno.estudiar()}")

print(f"\n\nEl nombre del Profesor 1 es: {profesor1._nombre}, su nivel de experiencia es: {profesor1._experiencia}, y su numero asignado es: {profesor1._num_profesor}. Estatus: {Profesor.impartir()}")
print(f"\nEl nombre del Profesor 2 es: {profesor2._nombre}, su nivel de experiencia es: {profesor2._experiencia}, y su numero asignado es: {profesor2._num_profesor}. Estatus: {Profesor.evaluar()}")

print(f"\n\nEl nombre del curso 1 es: {curso1._nombre}, el codigo de la clase es: {curso1._codigo}, y el credito es: {curso1._creditos}. Estatus: {Curso.asignar()}")
print(f"\nEl nombre del curso 2 es: {curso2._nombre}, el codigo de la clase es: {curso2._codigo}, y el credito es: {curso2._creditos}. Estatus: {Curso.asignar()}")