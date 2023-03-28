def testa_x_y(x, y):
        if x > y:
            resultado = 1
        return resultado

print(testa_x_y(10, 5))

numero = int(input('Digite um número: '))

if numero == 42:
    print('Resposta para a vida, o universo e tudo mais')
else:
    print('Um número qualquer')

numero = int(input('Digite um número: '))

if numero == 0:
    print('0 não é nem par, nem ímpar')
elif numero % 2 == 0:  # Resto da divisão de número por 2
    print('{0} é par'.format(numero))
else:
    print('{0} é ímpar'.format(numero))