from math import cos, sin, asin, sqrt, radians


def haversine(r, y1, a1, y2, a2):

    c_r_y1 = cos(radians(y1))
    c_r_y2 = cos(radians(y2))

    p1 = sqrt(sin(radians((y2 - y1) / 2)) ** 2 + c_r_y1 * c_r_y2 * sin(radians((a2 - a1) / 2)) ** 2)

    d = 2 * r * asin(p1)
    
    return d
