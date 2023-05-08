'''
Você escreveu um texto gigante e quando acabou,
descobriu que o CAPS LOCK estava ligado!
Todas as letras maiúsculas e minúsculas foram trocadas! 
Faça uma função que recebe um texto (String) e troca maiúsculas 
por minúsculas e vice-versa, devolvendo a String do texto original consertada.

O nome da sua função deve ser capsLock
'''

def capsLock(texto):
    novo_texto = ''

    for letra in texto:

        if letra.isupper():
            novo_texto += letra.lower()

        elif letra.islower():
            novo_texto += letra.upper()

        else:
            novo_texto += letra
            
    return novo_texto
    