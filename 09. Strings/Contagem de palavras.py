def conta_palavras(texto):

    dic = {}
    especiais = '?!.,'

    texto = texto.lower()

    for c in especiais:
        texto = texto.replace(c, '')

    palavras = texto.split()

    for pal in palavras:
        if pal not in dic:
            dic[pal] = 1
        
        else:
            dic[pal] += 1

    return dic
    