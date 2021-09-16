from numpy import zeros
import random

poblacion = [] #En esta lista voy a guardar a toda mi población
aptitud = [] #En esta lista voy a guardar los valores de aptitud

def CalAptitud(matrix): #Suma todos los elementos de la matriz que recibe para calcular su aptitud
    aptitud = 0
    dim = len(matrix)
    for row in range(dim):
        for col in range(dim):
            aptitud = aptitud + matrix[row][col]
    return aptitud

for i in range (0, 100): #Este for crea 100 individuos
    tablero = zeros((4,4))
    tablero[0][1] = 2
    tablero[0][0] = random.randrange(1,4)
    tablero[0][2] = 4
    tablero[0][3] = random.randrange(1,4)
    tablero[1][0] = 1
    tablero[1][1] = random.randrange(1,4)
    tablero[1][2] = random.randrange(1,4)
    tablero[1][3] = 3
    tablero[2][0] = 4
    tablero[2][1] = random.randrange(1,4)
    tablero[2][2] = random.randrange(1,4)
    tablero[2][3] = 2
    tablero[3][0] = random.randrange(1,4)
    tablero[3][1] = 1
    tablero[3][2] = 3
    tablero[3][3] = random.randrange(1,4)
    poblacion.append(tablero)
    aptitud.append(CalAptitud(tablero))

#poblacion[0][0][2] Así se accede al elemento 0 de población, específicamente a su coordenada [0][1]

print(poblacion[0])
print(aptitud[0])