import math
x = []
x.append(float(input('digite valor de x: ')))
x.append(float(input('digite valor de y: ')))
x.append(float(input('digite valor de z: ')))
#latitude
lat = math.atan2(x[1],x[0])
lat = math.degrees(lat)
#longitude
N=1
h = 0
aux = 1
a = 6378160
E = 0.00669454185
P = math.sqrt(x[0]**2+x[1]**2)
for i in range(10):
    teta = math.atan((x[2]/P)*((1-E*(N/(N+h)))**-1))
    h = ((P/math.cos(teta))-N)
    N = (a/(math.sqrt(1-E*math.sin(teta)**2)))
long = math.degrees(teta)
print('latitude ',lat)
print ('longitude',long)
print ('altura',h*1000)
input()

# Nota: 0.8
# O enunciado pede uma função
