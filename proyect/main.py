import random
import time
 #este codigo sirve para busqueda binaria y ingenua,sin embargo, para las busquedas binaria, las listas debe estar ordenada de forma ascendente.

def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1
     #range(len(lista)) -> 0, 1, 2, 3, ...., lent(lista)-1


def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0 #inicio de la lista.
    if limite_superior is None:
        limite_superior = len(lista)-1 #Final de la lista.

    if limite_superior < limite_inferior:
        return -1
    
    punto_medio = (limite_inferior + limite_superior) // 2
   
    #[1, 3, 5, 10, 12]
    # 0  1  2  3   4
    # punto_medio = (0 + 4) // 2 = 4, 4 // 2 = 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)
    

if __name__=='__main__':
    mi_lista = [1, 3, 5, 10, 12]
    print (busqueda_ingenua(mi_lista, 12))