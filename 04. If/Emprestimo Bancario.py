preco = int(input('Qual o valor da casa? '))
salario = int(input('Qual o seu salário? '))
anos = int(input('Você deseja pagar em quantos anos? '))

if preco / (anos * 12) > 0.3 * salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
