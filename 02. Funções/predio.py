import math
def altura_do_predio(comprimento, ângulo):
    altura = (math.tan(ângulo * 2 * math.pi / 360)) * comprimento
    return altura

print(altura_do_predio(10, 40))