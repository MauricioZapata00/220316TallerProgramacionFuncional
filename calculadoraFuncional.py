import numpy as np

suma = lambda a,b: a + b
resta = lambda a,b: a - b
def multiplicacion(a, b):
    sumArray = np.full(a,b)
    return np.sum(sumArray)

def division(a, b):
    if(b == 0):
        return "No se puede dividir por cero, la división por 0 no está definida"
    residuo = a
    cociente = 0
    while(residuo >= b):
        residuo = resta(residuo,b)
        #print(residuo)
        cociente += 1
    

    return "Cociente: " + str(cociente) + " ,y residuo: " + str(residuo)
    

print(suma(2,2))
print(resta(3,2))
print(multiplicacion(5, 4))
print(division(11, 4))
