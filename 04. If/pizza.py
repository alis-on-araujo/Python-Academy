tamanho = input('qual o tamanho da sua pizza? ')
borda = input('com borda? ')
queijo = input('queijo adicional? ')
refri = input('quer refrigerante? ')
sobremesa = input('quer sobremesa? ')

preco_total = 0

if tamanho == 'P':
    preco_tamanho = 50
if tamanho == 'M':
    preco_tamanho = 70
if tamanho == 'G':
    preco_tamanho = 90

preco_total = preco_tamanho

if borda == 'S':
    preco_total = preco_total + (preco_tamanho * 0.15)

if queijo == 'S':
    preco_total = preco_total + (preco_tamanho * 0.1)

if refri == 'S':
    preco_total += 12

if sobremesa == 'S':
    preco_total += 20
    if tamanho == 'G':
        preco_total *= 0.93

print('{0:.2f}'.format(preco_total))