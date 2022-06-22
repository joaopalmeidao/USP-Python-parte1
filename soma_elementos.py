def soma_elementos(lista):
    soma=0
    for item in lista:        
        soma=soma+item
    return soma
lista = [5, 2, 2, 7, 9, 5, 2, 4, 9, 10, 6, 6]
lista=soma_elementos(lista)
print(lista)
    
    