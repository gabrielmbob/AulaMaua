#ex1
from math import *

def distancia(x1,x2,y1,y2):
    distancia = sqrt((x2-x1)**2+(y2-y1)**2)
    return distancia

x1 = int(raw_input('Digite a coordenada X1 '))
y1 = int(raw_input('Digite a coordenada Y1 '))
x2 = int(raw_input('Digite a coordenada X2 '))
y2 = int(raw_input('Digite a coordenada Y2 '))
print 'A distancia entre os pontos eh',distancia(x1,x2,y1,y2)

#ex2
from math import *
lista = [(0,0),(2,4),(3,1),(-4,-6),(-7,-5)]
i = 0
j = i+1
def maiordist(lista):
    distancia = 0
    for i in range (len(lista)):
        x1 = lista[i][0]
        y1 = lista[i][1]
        for j in range (len(lista)):
            x2 = lista[j][0]
            y2 = lista[j][1]
            novadist = sqrt((x2-x1)**2+(y2-y1)**2)
            if (novadist > distancia):
                distancia = novadist
    print distancia
                
            
maiordist(lista) 

#ex3
from math import *


def polar(x,y):
    modulo = sqrt(x**2+y**2)
    teta = atan2(y,x)
    print ' o modulo eh {0} e o angulo {1}'.format (modulo,teta)


x1 = int(raw_input('Digite a coordenada X1 '))
y1 = int(raw_input('Digite a coordenada Y1 '))
x2 = int(raw_input('Digite a coordenada X2 '))
y2 = int(raw_input('Digite a coordenada Y2 '))
polar(x1,y1)
polar(x2,y2)

#ex4
from math import *

def retangulo(A,B,C):
    if (A+B <= C):
        print A,B,C
    else:
        area = A*B/2
        print 'A area eh: ',area
    
A = int(raw_input('Digite um valor A: '))
B = int(raw_input('Digite um valor B: '))
C = int(raw_input('Digite um valor C: '))
retangulo(A,B,C)

#ex5
from math import *



def geo(x,y,z):
    E = 0.00669454185
    a = 6378160

    P = sqrt(x**2+y**2)
    lat = atan2(y,x)
    aux = (z/P)*(1-E)**(-1)
    lon = atan(aux)
    for i in range (5) :
        N = a/(sqrt(1-(E*(sin(lon))**2)))
        h = (P/cos(lon))-N
        aux = (z/P)*((1-(E*N/(N+h))**(-1)))
        lon = atan(aux)
    lon = lon*180/pi
    print lon, lat, h


    
x = float(raw_input('Digite a coordenada X: '))
y = float(raw_input('Digite a coordenada Y: '))
z = float(raw_input('Digite a coordenada Z: '))
geo(x,y,z)

