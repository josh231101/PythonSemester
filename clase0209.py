m=35
n=3
comb = 0

def factorial(num):
    f=1
    for i in range(1, num+1):
        f= f * i
    return f

parte1 = factorial(m)
parte2 = factorial(m-n)
parte3 = factorial(n)

comb = parte1 / (parte2 * parte3)
print(comb)

# UNIVERSO M
# CANTIDAD DE N
#CUANTAS COMBINACIONES DIFERENTES SON EN UN GRUPO DE 35