def calculararea(base, altura):
    calcular = (base * altura) / 2
    return calcular

base = float(input("Ingrese la base de un rectángulo: "))
altura = float(input("Ingrese la altura de un rectángulo: "))
total = calculararea(base, altura)
print("El área es: ", total)