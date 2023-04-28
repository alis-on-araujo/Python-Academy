from math import pi

densa = 997

def will_it_float(P, R, r):
    
    boia = True
    
    vol = 2 * pi**2 * R * r **2
    densb = 10 ** 6 * P / vol

    if densb <= densa:
        boia = True
    
    elif densb > densa:
        boia = False

    return boia
