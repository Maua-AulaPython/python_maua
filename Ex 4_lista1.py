import math

x = []
for i in range(2):
    x.append(int(input('digite o valor do cateto: ')))
x.append(int(input('digite o valor da hipotenusa: ')))
if ((x[0]+x[1])>x[2]):
    area = x[0]*x[1]/2
    print('a area eh: ',area)
else:
    for i in range(len(x)):
        print('os valores inserido: ',x[i])
    print('nao eh triangulo retangulo')
input()

# Nota: 0.5
# O enunciado pede uma função
