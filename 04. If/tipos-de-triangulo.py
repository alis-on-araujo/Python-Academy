def classifica_triangulo(lado1, lado2, lado3):
    if lado1==lado2 and lado1!=lado3:
        return 'isósceles'
    elif lado1 == lado3 and lado1!=lado2:
        return 'isósceles'
    elif lado2==lado3 and lado1!=lado1:
        return 'isósceles'
    elif lado1==lado2==lado3:
        return 'equilátero'
    else:
        return 'escaleno'

print(classifica_triangulo(1, 3, 2))