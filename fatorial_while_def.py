def fat(n):
    n=int(input('Digite um númnero inteiro positivo: '))
    while n>=0:
        fatorial=1   
        while n>1:
            fatorial=fatorial*n
            n-=1
        print(fatorial)
        n=int(input('Digite um númnero inteiro positivo: '))

n=1
fat(n)