#Ejemplos de casting

entero = 1923
decimal = 12.39109210
booleano = True

e = str(entero)
d = str(decimal)
b = str(booleano)

print('entero' + e + ' decmial: ' + d + ' booleano: ' + b)

#Convierte un entero y un string a un punto decimal
entero2 = 900
cadenaString = '78.212'

a = float(entero2)
c = float(cadenaString)
print("Convertimos a float")
print(a , " " , c)

#Convierte de entero, decimal y string a booleano
entero3 = 0
string2 = ''
string3 = 'hola'
floatOne = -3.45
floatTwo = 0.0

booleanOne = bool(entero3)
booleanTwo = bool(string2)
booleanThree = bool(string3)
booleanFour = bool(floatOne)
booleanFive = bool(floatTwo)
print("Pasamos todo a boolean: ")
print(booleanOne , " " , booleanTwo , " " , booleanThree , " " , booleanFour , " " , booleanFive)
