def nivel_idh(idh):
    if idh < 0.350:
        idh = 'Sem dados'
    elif idh >= 0.350 and idh < 0.555:
        idh = 'Baixo'
    elif idh >= 0.555 and idh < 0.700:
        idh = 'Médio'
    elif idh >= 0.700 and idh < 0.800:
        idh = 'Alto'
    elif idh >= 0.800 and idh<= 1.000:
        idh = 'Muito Alto'
    return idh
