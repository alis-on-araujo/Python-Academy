'''
Escreva uma função que recebe um valor de distância, em km, percorrida por um veículo e o tempo gasto, 
em horas, para percorrer esta distância. A função retorna a velocidade média do veículo em km/h.
'''

def calcula_velocidade_media(distancia, tempo):
    vm = distancia / tempo
    return vm

vm = calcula_velocidade_media(100, 5)

print(vm)
