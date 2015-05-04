import math

def polar(x,y):
    r = math.sqrt((x[1]-x[0])**2+(y[1]-y[0])**2)
    teta = math.atan2((x[1]-x[0]),(y[1]-y[0]))
    teta = math.degrees(teta)
    print('raio ', r,'angulo ',teta)

x = []
y = []
for i in range(2):
    x.append(int(input('digite um valor de x: ')))
    y.append(int(input('digite um valor de y: ')))
polar(x,y)
input()

# Nota: 1.0
# Ok!
