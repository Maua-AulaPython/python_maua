x = []
soma = 0
y = 0
i=1
while (y >= 0):
          y = float(input('digite um numero: '))
          if y>=0:
               x.append(y)
if len(x)==0:
     print ('nenhum valor inserido')
else:
     for i in range(0,len(x)):
          soma = soma + x[i]
     media = soma/len(x)
     print (media)
input()

# Nota: 1.0
# Comentario. Muito bom. Vamos evitar o ultimo input() ? :)
