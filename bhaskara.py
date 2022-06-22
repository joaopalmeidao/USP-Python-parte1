import math


a=float(input('Qual valor de a? '))
b=float(input('Qual valor de b? '))
c=float(input('Qual valor de c? '))

delta=b**2-4*a*c

if delta >= 0:
    raiz_delta=math.sqrt(delta)
    x1=(-b+raiz_delta)/2*a
    x2=(-b-raiz_delta)/2*a

    if delta > 0:
        if x1 < x2:
            print('as raízes da equação são ',x1,'e',x2)
        else:
            print('as raízes da equação são ',x2,'e',x1)
    if delta == 0:
        print('a raiz desta equação é ',x1)
else:
    print('esta equação não possui raízes reais')

