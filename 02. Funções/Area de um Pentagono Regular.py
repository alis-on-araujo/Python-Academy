from math import tan, radians

tg36 = tan(radians(36))
print(tg36)

def area_pentagono(lado):
    apotema = lado/(4*tg36)
    area = 5*lado*apotema
    return area
