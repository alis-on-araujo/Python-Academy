cigarros = int(input('Quantos cigarros você fuma por dia?'))
anos = int(input('Há quantos anos você fuma?'))

cigarros_dia_em_horas = cigarros * 10 / 60 
#aqui está em horas
anos_fumo = cigarros_dia_em_horas * anos * 365

texto = 'Você tem {0} dias a menos de vida'. format((anos_fumo)/24)
print(texto)
