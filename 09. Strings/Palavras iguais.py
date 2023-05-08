def palavras_sao_iguais(string):

    palavras = string.split('-')

    if len(palavras) != 2:
        return False
        
    if palavras[0] == palavras[1]:
        return True
    else:
        return False