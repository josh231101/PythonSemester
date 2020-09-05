import math

def convertir_segundos(segundos):
    horas = math.floor(segundos / (60 * 60))
    minutos = math.floor((segundos / 60) % 60)
    segundos = round(segundos % 60)
    return horas, minutos, segundos


def main():
    r = convertir_segundos(9814)
    print(str(r[0]) + " horas " + str(r[1]) + " minutos " + str(r[2]) + " segundos")


main()