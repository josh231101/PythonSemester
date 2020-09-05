#Cuantas combinaciones son posibles en un grupo de 35 alumnos el cula desea formar un comité de 3 integrantes.

#formula número combinatorio
"""
C(m,n) = m! / (m-n)!n!
"""
def factorial(m):
    f=1
    for i in range(1, m+1):
        f *=i
    return f
def numeroCombinatorio(m,mn,n):
    numeroCombinatorio = m / (mn*n)
    return numeroCombinatorio

def calcNumCombinatorio(m,n):
   numeroCombinatorio = (factorial(m))/(factorial(m-n) * factorial(n))
   return numeroCombinatorio

#donde m = 35 y n = 3
#Variables iniciales
m=35 #Numero de alumnos
n=3 #Cantidad de miembros posibles en el comité
Comb = 1 #Combinaciones posibles

f=1
#Sacar factorial de m
for i in range(1, m+1):
    f*=i
p1 = f

#Sacar factorial de (m-n)
f = 1
r = m-n
for i in range(1, r + 1):
    f *= i
p2 = f

#Obtenemos el n!
f=1
for i in range(1, n+1):
    f *= i
p3 = f

Comb = p1/(p2*p3)
print(Comb)

factorialM = factorial(m)
factorialMn = factorial(r)
factorialN = factorial(n)
Comb = numeroCombinatorio(factorialM,factorialMn,factorialN)
print(Comb)

combinations = calcNumCombinatorio(m,n)
print(combinations)

for i in range(10):
    print(i)



