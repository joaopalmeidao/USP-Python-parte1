largura=int(input('Digite a largura: '))
altura=int(input('Digite a altura: '))
linha=1
coluna=1
while linha<=altura:
    while coluna<=largura:
        print('#', end='')
        coluna+=1
    linha+=1
    print()
    coluna=1