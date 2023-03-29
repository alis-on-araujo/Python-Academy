def valida_data(dia, mes, ano):
    # Verifica se o ano é bissexto ou não
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        bissexto = True
    else:
        bissexto = False

    # Verifica se o mês e o dia são válidos
    if mes < 1 or mes > 12:
        return False
    elif dia < 1:
        return False
    elif mes == 2:
        if bissexto:
            if dia > 29:
                return False
        elif dia > 28:
            return False
    elif mes in [4, 6, 9, 11]:
        if dia > 30:
            return False
    else:
        if dia > 31:
            return False

    # Se passou em todas as verificações, retorna True
    return True
