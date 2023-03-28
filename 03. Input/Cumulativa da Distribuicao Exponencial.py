from math import e

a = float(input("Qual a taxa (λ)? "))
x = float(input("Qual x, para calcular F(λ, x)? "))

res = 1 - (e ** (-a * x))

print('{0:.4f}'.format(res))
