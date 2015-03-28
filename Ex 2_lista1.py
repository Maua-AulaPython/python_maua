import math

x = []
y = []
res = -1
i=0
n = int(input('digite o número de pontos: '))
for i in range(n):
    x.append(int(input('digite o valor de x: ')))
    y.append(int(input('digite o valor de y: ')))
    for i in range(len(x)):
        for j in range(len(x)):
            aux = math.sqrt((x[j]-x[i])**2+(y[j]-y[i])**2)
            if res < aux:
                res = aux
print ('a maior distancia eh: ',res)
input()
