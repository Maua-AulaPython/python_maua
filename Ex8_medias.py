import os
x = []
soma = 0
y = 0
i=1

def maior(x):
    aux = 0
    for i in range(len(x)):
        if aux < x[i]:
            aux = x[i]
    return aux

while (y >= 0):
     while True:
          try:
               y = float(input('digite um numero: '))
               break
          except:
               print('numero invalido')
     if y>=0:
          x.append(y)
os.system('cls')
if len(x)==0:
     print ('nenhum valor inserido')
else:
     for i in range(0,len(x)):
          print ('nota [' ,i+1, ']: ',x[i])
          soma = soma + x[i]
     media = soma/len(x)
     print('maior nota: ',maior(x))
     print ('media: ', media)
input()

#Nota: 1.0
#Comentario: cuidado com funcoes do os (cls). Input final desnecessario
