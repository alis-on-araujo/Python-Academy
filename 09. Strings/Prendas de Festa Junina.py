def contabiliza(doacoes):

    dic = {}

    for lista in doacoes.values():

        for prenda in lista:
            idx = prenda.find(' ') #primeira ocorrência do espaço

            qtd = int(prenda[:idx]) #slice entre o começo e o 1o espaço
            nome = prenda[idx+1:] #slice entre a partir do 1o espaço e o final

            if nome not in dic:
                dic[nome] = qtd
            
            else:
                dic[nome] += qtd

    return dic