def soma_impares(lista):
    soma = 0
    
    for a in lista:
        if a % 2 != 0:
            soma += a
            
    return soma
