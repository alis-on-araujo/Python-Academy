'''
Faça uma função que recebe um peso em libras e devolve o seu equivalente em quilogramas.

Utilize a constante: 0.45359237

O nome da sua função deve ser libras_para_kg
'''

def libras_para_kg(lb):
    kg = lb * 0.45359237
    return kg

res = libras_para_kg(1)
print(res)
