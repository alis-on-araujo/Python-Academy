dias = int(input('Quantidade de dias'))
horas = int(input('Quantidade de horas'))
minutos = int(input('Quantidade de minutos'))
segundos = int(input('Quantidade de segundos'))

dias_seg = dias * 86400
horas_seg = horas * 3600
min_seg = minutos * 60

print(dias_seg + horas_seg + min_seg + segundos)
