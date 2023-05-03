tamanho = input("Qual o tamanho? ")
borda = input("Borda recheada? ")
queijo = input("Queijo adicional? ")
refri = input("Refrigerante? ")
sobremesa = input("Sobremesa? ")

preco_total = 0

if tamanho == 'P':
    preco_tamanho = 50
elif tamanho == 'M':
    preco_tamanho = 70
elif tamanho == 'G':
    preco_tamanho = 90

preco_total = preco_tamanho

if borda == 'S':
    preco_total = preco_total + (preco_tamanho * 0.15)

if queijo == 'S':
    preco_total += (preco_tamanho * 0.10)

if refri == 'S':
    preco_total += 12

if sobremesa == 'S':
    preco_total += 20
    if tamanho == 'G':
        preco_total = preco_total*0.93

print("{0:.2f}".format(preco_total))


