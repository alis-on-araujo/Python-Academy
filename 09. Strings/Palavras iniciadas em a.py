palavras = []

continua = True

while continua:
    palavra = input('Digite uma palavra (ou "fim" para encerrar): ')
    if palavra == 'fim':
        continua = False
    palavras.append(palavra)

for palavra in palavras:
    if palavra[0] == 'a':
        print(palavra)