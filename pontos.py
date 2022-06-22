import math
x1=float(input('Digite a coordenada x do primeiro plano cartesiano: '))
y1=float(input('Digite a coordenada y do primeiro plano cartesiano: '))
x2=float(input('Digite a coordenada x do segundo plano cartesiano: '))
y2=float(input('Digite a coordenada y do segundo plano cartesiano: '))

raiz=(x1-x2)**2+(y1+y2)**2

distancia=math.sqrt(raiz)

if distancia >= 10:
    print('longe')
else:
    print('perto')





    
