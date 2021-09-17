from numpy import zeros
import random

poblacion = [] #En esta lista voy a guardar a toda mi población
aptitud = [] #En esta lista voy a guardar los valores de aptitud
sigpoblacion = []
sigaptitud = []

def imprimirMatriz(individuo):
    tablero = zeros((4,4))
    tablero[0][1] = 2
    tablero[0][0] = individuo[0]
    tablero[0][2] = 4
    tablero[0][3] = individuo[1]
    tablero[1][0] = 1
    tablero[1][1] = individuo[2]
    tablero[1][2] = individuo[3]
    tablero[1][3] = 3
    tablero[2][0] = 4
    tablero[2][1] = individuo[4]
    tablero[2][2] = individuo[5]
    tablero[2][3] = 2
    tablero[3][0] = individuo[6]
    tablero[3][1] = 1
    tablero[3][2] = 3
    tablero[3][3] = individuo[7]
    print(tablero)

def CalAptitud(individuo): #Suma todos los elementos de la matriz que recibe para calcular su aptitud
    aptitud = 0
    aptitud1 = 0
    aptitud2 = 0
    aptitud3 = 0
    aptitud4 = 0
    aptitud5 = 0
    aptitud6 = 0
    aptitud7 = 0
    aptitud8 = 0

    tablero = zeros((4,4))
    tablero[0][1] = 2
    tablero[0][0] = individuo[0]
    tablero[0][2] = 4
    tablero[0][3] = individuo[1]
    tablero[1][0] = 1
    tablero[1][1] = individuo[2]
    tablero[1][2] = individuo[3]
    tablero[1][3] = 3
    tablero[2][0] = 4
    tablero[2][1] = individuo[4]
    tablero[2][2] = individuo[5]
    tablero[2][3] = 2
    tablero[3][0] = individuo[6]
    tablero[3][1] = 1
    tablero[3][2] = 3
    tablero[3][3] = individuo[7]

    aptitud1 = tablero[0][0] + tablero[0][1] + tablero[0][2] + tablero[0][3]
    aptitud2 = tablero[1][0] + tablero[1][1] + tablero[1][2] + tablero[1][3]
    aptitud3 = tablero[2][0] + tablero[2][1] + tablero[2][2] + tablero[2][3]
    aptitud4 = tablero[3][0] + tablero[3][1] + tablero[3][2] + tablero[3][3]
    aptitud5 = tablero[0][0] + tablero[1][0] + tablero[2][0] + tablero[3][0]
    aptitud6 = tablero[0][1] + tablero[1][1] + tablero[2][1] + tablero[3][1]
    aptitud7 = tablero[0][2] + tablero[1][2] + tablero[2][2] + tablero[3][2]
    aptitud8 = tablero[0][3] + tablero[1][3] + tablero[2][3] + tablero[3][3]

    if(aptitud1-10 != 0):
        if(aptitud1-10 <0):
            aptitud = aptitud + (aptitud1-10)*(-1)
            #print("suma", (aptitud1-10)*(-1))
        else:
            aptitud = aptitud + aptitud1-10
            #print("suma", aptitud1-10)
    if(aptitud2-10 != 0):
        if(aptitud2-10 <0):
            aptitud = aptitud + (aptitud2-10)*(-1)
            #print("suma", (aptitud2-10)*(-1))
        else:
            aptitud = aptitud + aptitud2-10
            #print("suma", aptitud2-10)
    if(aptitud3-10 != 0):
        if(aptitud3-10 <0):
            aptitud = aptitud + (aptitud3-10)*(-1)
            #print("suma", (aptitud3-10)*(-1))
        else:
            aptitud = aptitud + aptitud3-10
            #print("suma", aptitud3-10)
    if(aptitud4-10 != 0):
        if(aptitud4-10 <0):
            aptitud = aptitud + (aptitud4-10)*(-1)
            #print("suma", (aptitud4-10)*(-1))
        else:
            aptitud = aptitud + aptitud4-10
            #print("suma", aptitud4-10)
    if(aptitud5-10 != 0):
        if(aptitud5-10 <0):
            aptitud = aptitud + (aptitud5-10)*(-1)
            #print("suma", (aptitud5-10)*(-1))
        else:
            aptitud = aptitud + aptitud5-10
            #print("suma", aptitud5-10)
    if(aptitud6-10 != 0):
        if(aptitud6-10 <0):
            aptitud = aptitud + (aptitud6-10)*(-1)
            #print("suma", (aptitud6-10)*(-1))
        else:
            aptitud = aptitud + aptitud6-10
            #print("suma", aptitud6-10)
    if(aptitud7-10 != 0):
        if(aptitud7-10 <0):
            aptitud = aptitud + (aptitud7-10)*(-1)
            #print("suma", (aptitud7-10)*(-1))
        else:
            aptitud = aptitud + aptitud7-10
            #print("suma", aptitud7-10)
    if(aptitud8-10 != 0):
        if(aptitud8-10 <0):
            aptitud = aptitud + (aptitud8-10)*(-1)
            #print("suma", (aptitud8-10)*(-1))
        else:
            aptitud = aptitud + aptitud8-10
            #print("suma", aptitud8-10)
    return aptitud

def mejorInd(aptitud):
    mejorApt = 100
    indice = 0
    for i in range(0,100):
        if(aptitud[int(i)] <= mejorApt):
            mejorApt = aptitud[int(i)]
            indice = i
    return indice

for i in range (0, 100): #Este for crea 100 individuos
    tablero = zeros(8)
    tablero[0] = random.randrange(1,5)
    tablero[1] = random.randrange(1,5)
    tablero[2] = random.randrange(1,5)
    tablero[3] = random.randrange(1,5)
    tablero[4] = random.randrange(1,5)
    tablero[5] = random.randrange(1,5)
    tablero[6] = random.randrange(1,5)
    tablero[7] = random.randrange(1,5)
    poblacion.append(tablero)
    aptitud.append(CalAptitud(tablero))

#print(poblacion[0])
#imprimirMatriz(poblacion[0])
#print(aptitud[0])

sigpoblacion = poblacion
sigaptitud = aptitud

#print("Len", len(sigpoblacion))

#print(aptitud)
#print(mejorInd(aptitud))
#print(aptitud[mejorInd(aptitud)])
sigpoblacion[0] = poblacion[mejorInd(aptitud)]
sigaptitud[0] = aptitud[mejorInd(aptitud)]
#print(sigpoblacion[0])
#print(sigaptitud[0])

gen = 1
while(gen <= 100):
    poblacion = sigpoblacion
    aptitud = sigaptitud
    j = 1
    #print("gen", gen)
    while(j < 100):
        #print("j", j)
        p = random.randrange(2,6)
        #print(p)
        valor = zeros(p)
        mejorApt = 100
        for i in range (0, p):
            valor[i] = random.randrange(0,100)
                    #torneo.append(poblacion[valor[i]])
        for i in range (0,p):
            item = int(valor[i])
            if(CalAptitud(poblacion[item]) <= mejorApt): #Revisa si la aptitud del elemento i de la población es menor a la mejor aptitud actual
                mejorApt = valor[i]
        padre1 = mejorApt #mejorApt es la posición en la lista población que contiene al padre

        p = random.randrange(2,6)
                #torneo2 = []
        valor = zeros(p)
        mejorApt2 = 100
        for i in range (0, p):
            valor[i] = random.randrange(0,100)
                    #torneo2[i] = poblacion[valor[i]]
        for i in range (0, p):
            item = int(valor[i])
            if(CalAptitud(poblacion[item]) <= mejorApt2):
                mejorApt2 = valor[i]
        padre2 = mejorApt2 #mejorApt es la posición en la lista población que contiene al padre
        #print("Padre 1:", poblacion[int(mejorApt)])
        #print("Padre 2:", poblacion[int(mejorApt2)])

        padre1 = poblacion[int(mejorApt)]
        padre2 = poblacion[int(mejorApt2)]
        hijo1 = zeros(8)
        hijo2 = zeros(8)
        proba = random.randrange(1, 101)
        if(proba <= 90): #Si el número es menor a 90 se hará la cruza de un punto.

            hijo1[0] = padre1[0]
            hijo1[1] = padre1[1]
            hijo1[2] = padre1[2]
            hijo1[3] = padre1[3]
            hijo1[4] = padre2[4]
            hijo1[5] = padre2[5]
            hijo1[6] = padre2[6]
            hijo1[7] = padre2[7]

            hijo2[0] = padre2[0]
            hijo2[1] = padre2[1]
            hijo2[2] = padre2[2]
            hijo2[3] = padre2[3]
            hijo2[4] = padre1[4]
            hijo2[5] = padre1[5]
            hijo2[6] = padre1[6]
            hijo2[7] = padre1[7]

        if(proba <= 10): #Mutación
            aleatorio = random.randrange(0,8)
            if(hijo1[aleatorio] == 4):
                hijo1[aleatorio] = 1
            else:
                hijo1[aleatorio] = hijo1[aleatorio] + 1
            if(hijo2[aleatorio] == 4):
                hijo2[aleatorio] = 1
            else:
                hijo2[aleatorio] = hijo2[aleatorio] + 1

        sigpoblacion[j] = hijo1
        sigaptitud[j] = CalAptitud(hijo1)
        if(j < 99):
            sigpoblacion[j+1] = hijo2
            sigaptitud[j+1] = CalAptitud(hijo2)

        j = j + 2
    #identificar al mejor individuo
    MejorIndividuo = mejorInd(sigaptitud)
    sigpoblacion[0] = sigpoblacion[MejorIndividuo]
    sigaptitud[0] = sigaptitud[MejorIndividuo]
    gen = gen + 1

MejorIndividuo = mejorInd(sigaptitud)
print(imprimirMatriz(sigpoblacion[MejorIndividuo]))
print(sigaptitud[MejorIndividuo])