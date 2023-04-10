def numero_no_indice(lista):

    listaind = []

    for a in lista:

        if a == lista.index(a):
            listaind.append(a)
    
    return listaind
