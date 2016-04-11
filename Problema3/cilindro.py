import sys, os
import numpy as np  
import math as m

def distancia(x,y):
	difX = x[0] - y[0]
	difY = x[1] - y[1]
	difZ = x[2] - y[2]
	dis = m.sqrt(pow(difX,2) + pow(difY,2) + pow(difZ,2))
	return dis

def resta(x,y):
	difX = x[0] - y[0]
	difY = x[1] - y[1]
	difZ = x[2] - y[2]
	return [difX, difY, difZ]	

def suma(x,y):
	difX = x[0] + y[0]
	difY = x[1] + y[1]
	difZ = x[2] + y[2]
	return [difX, difY, difZ]	

def prodEscalar(x,k):
	difX = x[0] * k 
	difY = x[1] * k
	difZ = x[2] * k 
	return [difX, difY, difZ]	

def coseno(u,v):
	arriba = u[0]*v[0] +u[1]*v[1] +u[2]*v[2]
	abajo1  = m.sqrt(pow(u[0],2)+pow(u[1],2)+pow(u[2],2))  
	abajo2  = m.sqrt(pow(v[0],2)+pow(v[1],2)+pow(v[2],2))  
	mult = abajo1 * abajo2
	return arriba / mult

def prodVectorial(u,v):
	wx = u[1]*v[2] - u[2]*v[1]
	wy = u[2]*v[0] - u[0]*v[2]
	wz = u[0]*v[1] - u[1]*v[0]
	return [wx, wy, wz]

def normalizar(mag,dirEje):
	x = dirEje[0] / mag
	y = dirEje[1] / mag
	z = dirEje[2] / mag
	return [x,y,z]

myFile =  open('cilindro.txt')
lines = myFile.readlines()
lines = map(lambda x: x.split(' '),lines)
lines = map(lambda x: map( lambda y: float(y),x), lines)
countPoints = len(lines)

ejeX = map( lambda x:x[0],lines)
ejeY = map( lambda x:x[1],lines)
ejeZ = map( lambda x:x[2],lines)

minX = min(ejeX)
minY = min(ejeY)
minZ = min(ejeZ)


maxX = max(ejeX)
maxY = max(ejeY)
maxZ = max(ejeZ)

#punto centro del cilindro
centroX = (maxX + minX) / 2.0 
centroY = (maxY + minY) / 2.0 
centroZ = (maxZ + minZ) / 2.0 

centro = [centroX, centroY, centroZ]

minDis = 1000
minPoint = []
maxDis = 0
maxPoint = []
segMinPoint = []
segundoMinDis = 1000

for point in lines:
	disActual = distancia([centroX,centroY,centroZ],point)
	if minDis > disActual:
		minDis = disActual
		minPoint = point
	if maxDis < disActual:
		maxDis = disActual
		maxPoint = point 

for point in lines:
	disActual = distancia([centroX,centroY,centroZ],point)
	if segundoMinDis > disActual and point != minPoint:
		segundoMinDis = disActual
		segMinPoint = point

cero = [0,0,0]
vectorCentro1 = resta(minPoint, centro)
vectorCentro2 = resta(segMinPoint, centro)

dirEje = prodVectorial(vectorCentro1, vectorCentro2)
magnitudDirEje = distancia(cero, dirEje)
dirEjeTrasladado = suma(dirEje,centro)
dirEjeNormalizado = normalizar(magnitudDirEje,dirEje)

maxDis = distancia(maxPoint, centro)
vectorDis = resta(maxPoint, centro)
altura = 2*(m.sqrt(pow(maxDis,2) - pow(minDis,2)))
angulo = m.pi - m.acos(dirEjeNormalizado[2])

print "angulo"
print angulo
print "altura"
print altura
print "radio"
print minDis 

