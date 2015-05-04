import math

x = []
y = []
i=0
for i in range(2):
    x.append(int(input('digite o valor de x: ')))
    y.append(int(input('digite o valor de y: ')))
res = math.sqrt((x[1]-x[0])**2+(y[1]-y[0])**2)
print('a distancia entre os pontos eh: ',res)
input()

# Nota 0.5
# O exercicio pede para escreve uma função, além que o input não é necessario
