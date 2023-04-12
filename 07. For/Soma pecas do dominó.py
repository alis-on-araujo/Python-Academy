def soma_pecas(jogo):

    soma = 0

    for pecas in jogo:
        for face in pecas:
            soma += face
    
    return soma
