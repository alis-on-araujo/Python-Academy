def calcula_aumento(sal):
    if sal > 1250:
        aumento = 0.1 * sal
    else:
        aumento = 0.15 * sal
    
    return aumento
