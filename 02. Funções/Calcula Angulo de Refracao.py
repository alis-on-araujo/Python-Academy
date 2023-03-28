from math import sin, radians, asin, degrees

def snell_descartes(n1, n2, teta1):
    teta2 = sin(radians(teta1)) * n1 / n2
    return degrees(asin(teta2))
