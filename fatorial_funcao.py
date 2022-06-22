def fatorial(n):
    fat=1
    while (n>1):
        fat=fat*n
        n=n-1
    return fat
    
def numero_binominal(n,k):
    return fatorial(n)/(fatorial(k)*fatorial(n-k))

def testa_fatorial():
    if fatorial(1)==1:
        print('Funciona para 1')
    else:
        print('Não funciona para 1')
    if fatorial(2)==2:
        print('Funciona para 2')
    else:
        print('Não funciona para 2')
    
