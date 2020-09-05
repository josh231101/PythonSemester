
print("Hello World")
x = 0
y = 1
if y == x:
    print(x, " es igual  ", y)
else:
    print(x, " no es igual a ", y )

"""
OPERADORES ARITMÉTICOS
"""
print("Digita tu nombre: ")
nombre = input()
print(nombre)

a = 4.5
b = 8
print("Suma: ", a+b)
print("Resta: ", b-a)
print("Multiplicacion: ", a*b)
print("Potencia: ", b**2)
print("Division: ", b/a)
print("Division truncada: ", b//a)
print("Módulo: ", b%a)

"""
OPERADORES DE ASIGNACIÓN
"""

#Tipo de dato String
a = "Hola"
print("String Original: ", a)

#Utilizamos operador de Asignación
a+= " Mundo"
print("String Actualizado ", a)

#Tipo de dato Integer
b=10
print("Integer original ", b)
b-=10
print("Integer Actualizado" ,b, "\n")

#Tipo de dato float
c = 15.5
print("Float original: ", c)
c /=5
print("Float Actualizado: " ,c ,"\n")

"""
BUILT-IN FUNCTIONS
"""
texto = input("Ingresa un texto: ")
print(texto)

print("Numero de letras en su texto: ",len(texto))

#EJERCICIO 1
cuenta = float(input("Ingrese la cantidad de cuenta: "))
nPersonas = float(input("Ingrese la cantidad de personas: "))

#Propina del 20%
propina = 0.2
propinaEnCuenta = cuenta * propina
cuenta += propinaEnCuenta


cuentaPorPersona = round((cuenta /nPersonas),2)
print("Cada uno deberá pagar: ",cuentaPorPersona)

#EJERCICIO 2
palabras = 80000
palabrasPorPagina = int(input("¿Cuántas palabras quieres por página? Escribe: "))
resultado = divmod(palabras , palabrasPorPagina)
print("Habra un total de: ", resultado[0], " paginas con un total al final de ", resultado[1], " palabras")

# CONDICIONALES

a = 5
b = 20
if a > b:
    print(a, " es mayor que ", b)
else:
    print(b, " es mayor que ", a)

#FORMA SIMPLIFICADA
"""
a = true
print("Es verdadero) if a else print(" Es falso")
"""

# CUENTO CORTO
sujeto = input("Escribe un medio de transporte: ")
lugar = input("Escribe un lugar: ")
edadAyudante = int(input("Escribe una edad: "))

if edadAyudante >= 70:
    ayudante = "azafata vieja"
else:
    ayudante = "azafata joven"

print("Iba un " + sujeto + " en el " + lugar + " cuando de repente sale la " + ayudante + " diciendo: ")
print("- Señoras y señores, esto ya valió, se nos quemaron todas las alas. ")
print(" Y toda la gente empezó a gritar como loca.")
print("-Pero tranquilos, tranquilos, todavía nos quedan muslitos y pechugas xdxdxd")








































