def remove_repetidos(lista):
    lista_final = []
    for item in lista:
        if item not in lista_final:
            lista_final.append(item)
    lista_final.sort()
    return lista_final
lista = [5, 2, 2, 7, 9, 5, 2, 4, 9, 10, 6, 6]
lista = remove_repetidos(lista)
print (lista)
    
    
    

