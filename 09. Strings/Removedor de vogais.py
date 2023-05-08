'''
Faça uma função que remove as vogais de um texto

O nome da sua função deve ser remove_vogais
'''

def remove_vogais(texto):

    vogais = 'aeiouAEIOU'

    novo_texto = ''

    for letra in texto:
        if letra not in vogais:
            novo_texto += letra

    return novo_texto