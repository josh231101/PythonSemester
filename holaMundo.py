import CONSTANTES

# Declaracion de variables implícita
nombre = "Juan Garcia" #Cadena de carac
edad = 22 #Entero
estatura = 1.75 #Flotante
peso = 780.0 # Flotante
sobrepreso = "Resultado"

print(CONSTANTES.DB_NAME)
print("El nombres es" + nombre, edad, estatura)

if nombre == "Juan Garcia": #Evaluacion lógica
    print("Es correcto se llama: " + nombre)
else :
    print("no se llama Juan Garcia , su nombre es; " + nombre)

# *********  LOS RESULTADOS DE LA EVALUACIÓN SON MUTUAMENTE EXCLUYENTES **************

if peso>=120 :
    sobrepeso = "tiene sobrepeso"
else :
    sobrepreso = "no tiene sobrepeso"

print(nombre + sobrepeso)


#USAMOS EL BACKSLASH
variable = 'Este es un \'string\''
print(variable)

#TUPLAS
domicilio = ('Ave. Hidalgo', 5004, 208, 'Fracc. Petrolera Chariel')
print(domicilio[0])

#actividad de clase
persona = ('Juan', 'Ortiz', 21)
#Etiquetando elementos de la tupla
nombre , apellido, edad = persona
print('Nombre: ', nombre)
print('Apellido', apellido)
print('La edad de ', nombre, apellido, ' es ', edad, ' años')

nombre , edad = alumno = ('Jouse',24)
print(nombre)
print(edad)
