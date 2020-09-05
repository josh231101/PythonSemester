# Ejemplos de casting

#Programa para calcular el área de un cuadrado
print("Bienvenido al calculo de area del área")
print("Selecciona la opcion")
print("1. Calcular área de cuadrado\n2. Calcular área de triángulo")
#Usuario escoge opcion
opcion = input()


if opcion == "1":
    print("Introduce la medida del lado: ")
    lado = float(input())
    area = pow(lado, 2)
elif opcion == "2":
    print("Introduce la base: ")
    base = float(input())
    print("Introduce la altura: ")
    altura = float(input())
    area = base * altura / 2
else:
    print("No fue 1 o 2, intenta de nuevo")

print("El area es" + str(area))
