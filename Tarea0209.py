def factorial(number):
    f = 1
    for i in range(1, number+1):
        f *= i
    return f


def calcNumCombinatorio(m, n):
    comb = factorial(m) / (factorial(n) * factorial(m-n))
    return comb


def main():
    print("\t\t.: BIENVENIDO A LA CALCULADORA DE COMBINACIONES :.")
    m = int(input("Ingresa la cantidad del universo: "))
    n = int(input("Ingresa cuantos conformaran el grupo: "))
    comb = calcNumCombinatorio(m,n)
    print("En un universo de ", m, " existen ", comb, " combinaciones para formar un grupo de", n)


main()