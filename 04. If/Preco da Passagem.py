km = int(input('Quanto você deseja percorrer? '))
if km <= 200:
    valor = km * 0.50
    print('{0:.2f}'.format(valor))
elif km > 200:
    valor = 200 * 0.50 + (km - 200) * 0.45
    print('{0:.2f}'.format(valor))
