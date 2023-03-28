def testa_x_y(x, y):
        if x > y:
            print(1)
        elif x == y:
            print(0)
        elif x < y:
            print(-1)

print(testa_x_y(5, 5))

preco = int(input('Qual o valor da casa? '))
salario = int(input('Qual o seu salário? '))
anos = int(input('Você deseja pagar em quantos anos? '))

def parcela(preco, anos, salario):
    if preco / (anos * 12) > (0.3 * salario):
        print('Emprestimo não aprovado')
    else:
        print('Emprestimo aprovado')