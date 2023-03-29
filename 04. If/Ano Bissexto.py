def eh_bissexto(ano):
    # Verifica se o ano é bissexto ou não
    bissexto = True
    
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        bissexto = True
    else:
        bissexto = False

    return bissexto
